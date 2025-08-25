import random
from typing import List
from .data import names_data as data
from .data import patterns
from .utils import generate_random_letters

class CategoryGenerators:
    
    # Основные методы генерации
    @staticmethod
    def generate_4char(count: int, used_usernames: set) -> List[str]:
        """Генерация 4-символьных юзернеймов"""
        usernames = []
        patterns_list = ['cvcv', 'vcvc', 'cvc', 'vcv', 'vvcc', 'ccvv']
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 2):
            if len(usernames) >= count:
                break
                
            pattern = random.choice(patterns_list)
            username = ''
            
            for char in pattern:
                if char == 'c':
                    username += random.choice(consonants)
                elif char == 'v':
                    username += random.choice(vowels)
                else:
                    username += char
            
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    @staticmethod
    def generate_5char(count: int, used_usernames: set) -> List[str]:
        """Генерация 5-символьных юзернеймов"""
        usernames = []
        patterns_list = ['cvcvc', 'vcvcv', 'cvccv', 'cvvcc', 'ccvvc']
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 2):
            if len(usernames) >= count:
                break
                
            pattern = random.choice(patterns_list)
            username = ''
            
            for char in pattern:
                if char == 'c':
                    username += random.choice(consonants)
                elif char == 'v':
                    username += random.choice(vowels)
                else:
                    username += char
            
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    @staticmethod
    def generate_english_words(count: int, used_usernames: set) -> List[str]:
        """Генерация английских слов"""
        all_words = (data.SCAM_WORDS + data.NFT_KEYWORDS + data.TELEGRAM_KEYWORDS +
                    data.HUMAN_NAMES + data.GOD_NAMES + data.RAPPER_NAMES + data.ACTOR_NAMES +
                    data.BRAND_NAMES + data.GAME_NAMES + data.MEME_NAMES + data.CRYPTO_NAMES)
        
        valuable_words = [w for w in all_words if 4 <= len(w) <= 8]
        usernames = []
        
        for _ in range(count * 2):
            if len(usernames) >= count:
                break
                
            # Используем только одиночные слова, без комбинаций
            username = random.choice(valuable_words)
            
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # Основные методы для категорий
    @staticmethod
    def generate_scam(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.SCAM_WORDS)

    @staticmethod
    def generate_nft(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.NFT_KEYWORDS)

    @staticmethod
    def generate_telegram(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.TELEGRAM_KEYWORDS)

    @staticmethod
    def generate_humans(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.HUMAN_NAMES)

    @staticmethod
    def generate_gods(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.GOD_NAMES)

    @staticmethod
    def generate_rappers(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.RAPPER_NAMES)

    @staticmethod
    def generate_actors(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.ACTOR_NAMES)

    @staticmethod
    def generate_brands(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.BRAND_NAMES)

    @staticmethod
    def generate_games(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.GAME_NAMES)

    @staticmethod
    def generate_memes(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.MEME_NAMES)

    @staticmethod
    def generate_crypto(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_single_words(count, used_usernames, data.CRYPTO_NAMES)

    @staticmethod
    def _generate_single_words(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Генерация только одиночных слов без комбинаций"""
        usernames = []
        filtered_words = [w for w in word_list if 4 <= len(w) <= 12]
        
        # Используем только одиночные слова из списка
        for _ in range(count * 3):
            if len(usernames) >= count:
                break
                
            username = random.choice(filtered_words)
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # КРЕАТИВНЫЕ МЕТОДЫ ДЛЯ БЕСКОНЕЧНОЙ ГЕНЕРАЦИИ (без двойных имен)
    @staticmethod
    def generate_creative_patterns(count: int, used_usernames: set) -> List[str]:
        """Бесконечная генерация по паттернам"""
        usernames = []
        patterns_list = ['cvcv', 'vcvc', 'cvc', 'vcv', 'vvcc', 'ccvv', 
                        'cvcvc', 'vcvcv', 'cvccv', 'cvvcc', 'ccvvc']
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 3):
            if len(usernames) >= count:
                break
                
            pattern = random.choice(patterns_list)
            username = ''
            
            for char in pattern:
                if char == 'c':
                    username += random.choice(consonants)
                elif char == 'v':
                    username += random.choice(vowels)
                else:
                    username += char
            
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    @staticmethod
    def generate_creative_words(count: int, used_usernames: set) -> List[str]:
        """Креативная генерация слов без двойных имен"""
        usernames = []
        
        # Используем паттерны вместо комбинаций слов
        patterns_list = ['cvcvcv', 'vcvcvc', 'cvcvcv', 'vcvcvcv']
        vowels = 'aeiou'
        consonants = 'bcdfghjklmnpqrstvwxyz'
        
        for _ in range(count * 4):
            if len(usernames) >= count:
                break
                
            pattern = random.choice(patterns_list)
            username = ''
            
            for char in pattern:
                if char == 'c':
                    username += random.choice(consonants)
                elif char == 'v':
                    username += random.choice(vowels)
                else:
                    username += char
            
            # Добавляем суффиксы для разнообразия
            if random.random() < 0.3:
                suffix = random.choice(['er', 'or', 'ar', 'ist', 'ian', 'able', 'ible', 'ful', 'less', 'ness'])
                username = username + suffix
            
            if len(username) > 12:
                username = username[:12]
            
            if username not in used_usernames and 4 <= len(username) <= 12:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # Креативные методы для каждой категории (без двойных имен)
    @staticmethod
    def generate_creative_scam(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.SCAM_WORDS)

    @staticmethod
    def generate_creative_nft(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.NFT_KEYWORDS)

    @staticmethod
    def generate_creative_telegram(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.TELEGRAM_KEYWORDS)

    @staticmethod
    def generate_creative_names(count: int, used_usernames: set) -> List[str]:
        names = data.HUMAN_NAMES + data.GOD_NAMES + data.RAPPER_NAMES + data.ACTOR_NAMES
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, names)

    @staticmethod
    def generate_creative_gods(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.GOD_NAMES)

    @staticmethod
    def generate_creative_rappers(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.RAPPER_NAMES)

    @staticmethod
    def generate_creative_actors(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.ACTOR_NAMES)

    @staticmethod
    def generate_creative_brands(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.BRAND_NAMES)

    @staticmethod
    def generate_creative_games(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.GAME_NAMES)

    @staticmethod
    def generate_creative_memes(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.MEME_NAMES)

    @staticmethod
    def generate_creative_crypto(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_with_suffixes(count, used_usernames, data.CRYPTO_NAMES)

    @staticmethod
    def _generate_creative_with_suffixes(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Генерация с дополнительными суффиксами и приставками"""
        usernames = []
        filtered_words = [w for w in word_list if 3 <= len(w) <= 8]
        
        # Приставки, которые будут добавляться к словам
        prefixes = ['pre', 'un', 're', 'ex', 'in', 'dis', 'anti', 'bio', 'auto', 'inter', 'sub']
        
        # Суффиксы
        suffixes = ['er', 'or', 'ist', 'ian', 'able', 'ible', 'ful', 'less', 'ness', 'ment', 'tion', 'sion', 'ity', 'ly']
        
        for _ in range(count * 4):
            if len(usernames) >= count:
                break
                
            # Выбираем базовое слово
            base_word = random.choice(filtered_words)
            
            # Добавляем случайный суффикс или приставку
            if random.random() < 0.6:
                # Добавляем суффикс
                suffix = random.choice(suffixes)
                username = base_word + suffix
            else:
                # Добавляем приставку
                prefix = random.choice(prefixes)
                username = prefix + base_word
            
            # Если длина больше 12, обрезаем
            if len(username) > 12:
                username = username[:12]
            
            # Проверяем, чтобы юзернейм был уникальным
            if username not in used_usernames and 4 <= len(username) <= 12:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames
