from rewards_container.rewards_container import RewardsContainer

if __name__ == '__main__':
    containers_number = 10
    container = RewardsContainer()
    for i in range(containers_number):
        container.getRewards()