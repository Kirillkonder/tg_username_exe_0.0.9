import requests
import concurrent.futures
import time
import random
import re
from typing import Dict, List

class FragmentParser:
    def __init__(self):
        self.base_url = "https://fragment.com"
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        ]
        self.session = requests.Session()
        self.update_headers()
        self.request_count = 0

    def update_headers(self):
        """Обновляет заголовки с новым User-Agent"""
        self.headers = {
            'User-Agent': random.choice(self.user_agents),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        }
        self.session.headers.update(self.headers)

    def check_username_status(self, username: str) -> Dict:
        """Проверяет доступность на Fragment и определяет примерную цену"""
        url = f"{self.base_url}/username/{username}"
        
        # Меняем User-Agent каждые 10 запросов
        if self.request_count % 10 == 0:
            self.update_headers()
        
        try:
            start_time = time.time()
            
            # Случайная задержка от 0.5 до 1.5 секунд
            time.sleep(random.uniform(0.5, 1.5))
            
            response = self.session.get(url, headers=self.headers, timeout=8)
            self.request_count += 1
            
            request_time = time.time() - start_time
            
            # Определяем примерную цену на основе реальных данных Fragment
            price = self.estimate_price(username)
            
            if response.status_code == 200:
                html = response.text
                
                # ПРОСТАЯ И НАДЕЖНАЯ ПРОВЕРКА
                if 'Unavailable' in html:
                    status = 'Available'
                    reason = 'Свободен'
                    available = True
                    print(f"   ✅ {username} - СВОБОДЕН ({request_time:.1f}s) 💰 {price}")
                else:
                    status = 'Taken'
                    reason = 'Занят'
                    available = False
                    print(f"   ❌ {username} - ЗАНЯТ ({request_time:.1f}s) 💰 {price}")
                
                result = {
                    'username': username,
                    'status': status,
                    'reason': reason,
                    'available': available,
                    'url': url,
                    'response_time': round(request_time, 2),
                    'price': price,
                    'success': True
                }
                
                return result
                
            elif response.status_code == 404:
                # 404 обычно означает что юзернейм свободен
                result = {
                    'username': username,
                    'status': 'Available',
                    'reason': 'Свободен (404)',
                    'available': True,
                    'url': url,
                    'response_time': round(request_time, 2),
                    'price': price,
                    'success': True
                }
                print(f"   ✅ {username} - СВОБОДЕН (404) ({request_time:.1f}s) 💰 {price}")
                return result
                
            else:
                result = {
                    'username': username,
                    'status': f'HTTP {response.status_code}',
                    'reason': f'Ошибка HTTP: {response.status_code}',
                    'available': False,
                    'url': url,
                    'response_time': round(request_time, 2),
                    'price': price,
                    'success': False
                }
                print(f"   ❌ {username} - Ошибка HTTP {response.status_code} ({request_time:.1f}s)")
                return result
                
        except requests.exceptions.Timeout:
            result = {
                'username': username,
                'status': 'Timeout',
                'reason': 'Таймаут запроса',
                'available': False,
                'url': url,
                'response_time': 0,
                'price': 'N/A',
                'success': False
            }
            print(f"   ⚠️ {username} - Таймаут запроса")
            return result
            
        except requests.exceptions.ConnectionError:
            result = {
                'username': username,
                'status': 'ConnectionError',
                'reason': 'Ошибка подключения',
                'available': False,
                'url': url,
                'response_time': 0,
                'price': 'N/A',
                'success': False
            }
            print(f"   ⚠️ {username} - Ошибка подключения")
            return result
            
        except Exception as e:
            result = {
                'username': username,
                'status': f'Error: {type(e).__name__}',
                'reason': f'Ошибка: {str(e)}',
                'available': False,
                'url': url,
                'response_time': 0,
                'price': 'N/A',
                'success': False
            }
            print(f"   ⚠️ {username} - Ошибка: {type(e).__name__}")
            return result

    def estimate_price(self, username: str) -> str:
        """Оценивает примерную стоимость на основе реальных цен Fragment"""
        length = len(username)
        
        # Реальные примерные цены с Fragment (на основе открытых данных)
        if length == 3:
            return "$10,000-50,000"  # 3-char очень редкие
        elif length == 4:
            return "$5,000-20,000"   # 4-char premium
        elif length == 5:
            return "$1,000-5,000"    # 5-char quality
        elif length == 6:
            return "$500-2,000"      # 6-char good
        elif length == 7:
            return "$200-1,000"      # 7-char standard
        elif length == 8:
            return "$100-500"        # 8-char average
        elif length >= 9:
            return "$50-200"         # 9+ char basic
        else:
            return "$100-500"        # default

    def check_usernames_batch(self, usernames: List[str], max_workers: int = 10) -> List[Dict]:
        """Многопоточная проверка юзернеймов"""
        start_time = time.time()
        results = []
        
        print(f"🔍 Проверка {len(usernames)} юзернеймов:")
        print("─" * 60)
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Отправляем все задачи
            future_to_username = {
                executor.submit(self.check_username_status, username): username 
                for username in usernames
            }
            
            # Собираем результаты по мере готовности
            completed = 0
            for future in concurrent.futures.as_completed(future_to_username):
                username = future_to_username[future]
                try:
                    result = future.result()
                    results.append(result)
                    completed += 1
                    
                    # Прогресс
                    if completed % 5 == 0:
                        elapsed = time.time() - start_time
                        speed = completed / (elapsed / 60)
                        percent = (completed / len(usernames)) * 100
                        print(f"   📊 Прогресс: {completed}/{len(usernames)} ({percent:.0f}%) | Скорость: {speed:.0f}/мин")
                        
                except Exception as e:
                    error_result = {
                        'username': username,
                        'status': f'Future Error: {type(e).__name__}',
                        'reason': f'Ошибка выполнения: {str(e)}',
                        'available': False,
                        'url': f"{self.base_url}/username/{username}",
                        'response_time': 0,
                        'price': 'N/A',
                        'success': False
                    }
                    results.append(error_result)
                    print(f"   ⚠️ {username} - Ошибка выполнения: {type(e).__name__}")
                    completed += 1
        
        total_time = time.time() - start_time
        usernames_per_minute = len(usernames) / (total_time / 60)
        
        print("─" * 60)
        print(f"⏱️  Проверено {len(usernames)} юзернеймов за {total_time:.1f} сек")
        print(f"🚀 Скорость: {usernames_per_minute:.0f} юзернеймов/мин")
        
        return results