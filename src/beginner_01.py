
BLOCK_CHAIN = []

def sample_module():
    """TODO: 유닛 스모크 테스트용 True 리턴 전용함수

    :returns: True

    """
    return True


def get_status():
    print(BLOCK_CHAIN)


def get_last_blockchain_value():
    return BLOCK_CHAIN[-1]


def add_value(transaction_amount, last_transaction=[1]):
    BLOCK_CHAIN.append([last_transaction, transaction_amount])
