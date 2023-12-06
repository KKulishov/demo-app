import redis

class RedisClient:
    def __init__(self, host, port, password):
        self.host = host
        self.port = port
        self.password = password
        self.connection = None

    def __enter__(self):
        # Подключаемся к Redis
        self.connection = redis.StrictRedis(
            host=self.host,
            port=self.port,
            password=self.password,
            decode_responses=True
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Закрываем соединение с Redis при выходе из контекста
        if self.connection:
            self.connection.close()


def write_to_redis(client):
    # Записываем данные в Redis
    data = {"test1": 1, "test2": 2, "test3": 3, "test4": 4, "test5": 5,
            "test6": 6, "test7": 7, "test8": 8, "test9": 9, "test10": 10,
            "test11": 11, "test12": 12, "test13": 13, "test14": 14, "test15": 15,
            "test16": 16, "test17": 17, "test18": 18, "test19": 19, "test20": 20}

    for key, value in data.items():
        client.connection.set(key, value)

def read_from_redis(client):
    # Считываем данные из Redis
    data = {}
    keys = ["test1", "test2", "test3", "test4", "test5",
            "test6", "test7", "test8", "test9", "test10",
            "test11", "test12", "test13", "test14", "test15",
            "test16", "test17", "test18", "test19", "test20"]

    for key in keys:
        value = client.connection.get(key)
        data[key] = int(value) if value is not None else None

    return data

# Пример использования
host = "your_redis_host"  # Замените на реальный хост Redis
port = 6379  # Порт Redis
password = "your_redis_password"  # Замените на реальный пароль Redis

# Используем контекстный менеджер with
with RedisClient(host, port, password) as redis_client:
    # Запись данных
    write_to_redis(redis_client)

    # Чтение данных
    data_from_redis = read_from_redis(redis_client)
    print(data_from_redis)