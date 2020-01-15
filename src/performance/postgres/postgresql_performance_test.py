from src.drivers.postgres.impls.postgres_repositories import CustomerPostgresRepository
from src.drivers.postgres.impls.postgres_repositories import EventPostgresRepository
from src.drivers.postgres.impls.postgres_repositories import OrderPostgresRepository
from src.performance.performance_test import BasePerformanceTest


class PostgreSQLPerformanceTest(BasePerformanceTest):
    def __init__(self, operations_number: int):
        super().__init__(
            operations_number, CustomerPostgresRepository(), EventPostgresRepository(), OrderPostgresRepository()
        )

    def present_results(self, draw_chart: bool) -> None:
        database_name = 'PostgreSQL'

        customers_table_results = self.test_customers_table()
        events_table_results = self.test_events_table()
        orders_table_results = self.test_orders_table()

        print('> PERFORMANCE TESTS RESULTS')
        print(f'> DATABASE TYPE: {database_name}')
        print(f'> Operations number: {self.operations_number}')

        print('')

        print(f'>> For {customers_table_results.table_name} table:')
        print(f'>>> Inserting {self.operations_number} customers: {customers_table_results.insert_time}s')
        print(f'>>> Get by id {self.operations_number} customers: {customers_table_results.get_by_id_time}s')
        print(f'>>> Get all {self.operations_number} customers: {customers_table_results.get_all_time}s')

        print('')

        print(f'>> For {events_table_results.table_name} table:')
        print(f'>>> Inserting {self.operations_number} events: {events_table_results.insert_time}s')
        print(f'>>> Get by id {self.operations_number} events: {events_table_results.get_by_id_time}s')
        print(f'>>> Get all {self.operations_number} events: {events_table_results.get_all_time}s')

        print('')

        print(f'>> For {orders_table_results.table_name} table:')
        print(f'>>> Inserting {self.operations_number} orders: {orders_table_results.insert_time}s')
        print(f'>>> Get by id {self.operations_number} orders: {orders_table_results.get_by_id_time}s')
        print(f'>>> Get all {self.operations_number} orders: {orders_table_results.get_all_time}s')

        if draw_chart:
            self.draw_bar_chart(database_name, customers_table_results, events_table_results, orders_table_results)
