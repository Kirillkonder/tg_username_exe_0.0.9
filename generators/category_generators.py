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
        for _ in range(count):
            pattern = random.choice(patterns.PATTERNS_4CHAR)
            username = patterns.generate_from_pattern(pattern)
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        return usernames

    @staticmethod
    def generate_5char(count: int, used_usernames: set) -> List[str]:
        """Генерация 5-символьных юзернеймов"""
        usernames = []
        for _ in range(count):
            pattern = random.choice(patterns.PATTERNS_5CHAR)
            username = patterns.generate_from_pattern(pattern)
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
        
        for _ in range(count):
            if random.random() < 0.7:
                username = random.choice(valuable_words)
            else:
                word1 = random.choice([w for w in valuable_words if len(w) <= 4])
                word2 = random.choice([w for w in valuable_words if len(w) <= 4])
                username = word1 + word2
            
            if username not in used_usernames and 4 <= len(username) <= 8:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # Основные методы для категорий
    @staticmethod
    def generate_scam(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.SCAM_WORDS, "scam")

    @staticmethod
    def generate_nft(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.NFT_KEYWORDS, "nft")

    @staticmethod
    def generate_telegram(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.TELEGRAM_KEYWORDS, "telegram")

    @staticmethod
    def generate_humans(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.HUMAN_NAMES, "humans")

    @staticmethod
    def generate_gods(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.GOD_NAMES, "gods")

    @staticmethod
    def generate_rappers(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.RAPPER_NAMES, "rappers")

    @staticmethod
    def generate_actors(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.ACTOR_NAMES, "actors")

    @staticmethod
    def generate_brands(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.BRAND_NAMES, "brands")

    @staticmethod
    def generate_games(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.GAME_NAMES, "games")

    @staticmethod
    def generate_memes(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.MEME_NAMES, "memes")

    @staticmethod
    def generate_crypto(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_from_list(count, used_usernames, data.CRYPTO_NAMES, "crypto")

    @staticmethod
    def _generate_from_list(count: int, used_usernames: set, word_list: List[str], category_name: str) -> List[str]:
        """Универсальный генератор из списка слов БЕЗ СМЕШИВАНИЯ КАТЕГОРИЙ"""
        usernames = []
        filtered_words = [w for w in word_list if 4 <= len(w) <= 12]
        
        # Используем только слова из своей категории
        for _ in range(count * 2):
            if len(usernames) >= count:
                break
                
            username = random.choice(filtered_words)
            if username not in used_usernames:
                usernames.append(username)
                used_usernames.add(username)
        
        # Если не хватило слов, создаем комбинации ТОЛЬКО из слов этой категории
        if len(usernames) < count:
            remaining = count - len(usernames)
            for _ in range(remaining * 3):
                if len(usernames) >= count:
                    break
                    
                # Комбинация 2 слов из ТОЙ ЖЕ категории
                if len(filtered_words) >= 2:
                    word1 = random.choice(filtered_words)
                    word2 = random.choice(filtered_words)
                    username = word1 + word2
                    
                    if len(username) > 12:
                        username = username[:12]
                    
                    if username not in used_usernames and 4 <= len(username) <= 12:
                        usernames.append(username)
                        used_usernames.add(username)
        
        return usernames

    # КРЕАТИВНЫЕ МЕТОДЫ ДЛЯ БЕСКОНЕЧНОЙ ГЕНЕРАЦИИ
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
        """Креативная генерация слов"""
        all_words = (data.SCAM_WORDS + data.NFT_KEYWORDS + data.TELEGRAM_KEYWORDS +
                    data.HUMAN_NAMES + data.GOD_NAMES + data.RAPPER_NAMES + data.ACTOR_NAMES +
                    data.BRAND_NAMES + data.GAME_NAMES + data.MEME_NAMES + data.CRYPTO_NAMES)
        
        return CategoryGenerators._generate_creative_combo(count, used_usernames, all_words)

    @staticmethod
    def _generate_creative_combo(count: int, used_usernames: set, word_list: List[str]) -> List[str]:
        """Универсальный креативный генератор комбинаций"""
        usernames = []
        
        for _ in range(count * 4):
            if len(usernames) >= count:
                break
                
            # Комбинация 2-3 слов
            num_words = random.randint(2, 3)
            if len(word_list) >= num_words:
                words = random.sample(word_list, num_words)
                username = ''.join(words)
            else:
                # Если слов мало, используем паттерны
                username = patterns.generate_from_pattern(random.choice(['cvcv', 'vcvc', 'cvcvc', 'vcvcv']))
            
            # Добавляем префикс или суффикс
            if random.random() < 0.4:
                if random.random() < 0.5:
                    username = random.choice(data.PREFIXES) + username
                else:
                    username = username + random.choice(data.SUFFIXES)
            
            if len(username) > 12:
                username = username[:12]
            
            if username not in used_usernames and 4 <= len(username) <= 12:
                usernames.append(username)
                used_usernames.add(username)
        
        return usernames

    # Креативные методы для каждой категории
    @staticmethod
    def generate_creative_scam(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.SCAM_WORDS)

    @staticmethod
    def generate_creative_nft(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.NFT_KEYWORDS)

    @staticmethod
    def generate_creative_telegram(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.TELEGRAM_KEYWORDS)

    @staticmethod
    def generate_creative_names(count: int, used_usernames: set) -> List[str]:
        names = data.HUMAN_NAMES + data.GOD_NAMES + data.RAPPER_NAMES + data.ACTOR_NAMES
        return CategoryGenerators._generate_creative_combo(count, used_usernames, names)

    @staticmethod
    def generate_creative_gods(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.GOD_NAMES)

    @staticmethod
    def generate_creative_rappers(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.RAPPER_NAMES)

    @staticmethod
    def generate_creative_actors(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.ACTOR_NAMES)

    @staticmethod
    def generate_creative_brands(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.BRAND_NAMES)

    @staticmethod
    def generate_creative_games(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.GAME_NAMES)

    @staticmethod
    def generate_creative_memes(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.MEME_NAMES)

    @staticmethod
    def generate_creative_crypto(count: int, used_usernames: set) -> List[str]:
        return CategoryGenerators._generate_creative_combo(count, used_usernames, data.CRYPTO_NAMES)