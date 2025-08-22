from tabulate import tabulate

from aggregate_module import JSONAggregateInterface




def main():
    interface = JSONAggregateInterface()
    tabular_data = interface.report(interface.parsed_args.get_report_value)

    print(tabulate(tabular_data=tabular_data, headers="keys"))



if __name__ == "__main__":
    main()
