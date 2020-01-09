from drivers.mysql.driver import MySQLDriver


def main():
    print("Welcome in Database Comparator")
    mysql_driver = MySQLDriver()
    mysql_driver.run_tests()


if __name__ == '__main__':
    main()
