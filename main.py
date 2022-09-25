entitlements = ("AdminUsers", "RestoreUsers")
validusers = ("'user1', 'user2', 'user3', 'user4'", "'user5', 'user6', 'user7', 'user8'")

if __name__ == '__main__':
    template = open('config_template.py', 'r')
    config = open('config.py', 'w')
    for line in template:
        for entitlement, users in zip(entitlements, validusers):
            line = line.replace(entitlement, users)
        config.write(line)
    template.close()
    config.close()




