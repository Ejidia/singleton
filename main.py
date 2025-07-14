# main.py
# Main entry point that calls both modules (app1 and app2)

from app1 import process_data,save_results


def main():
    # Call function from app1
    process_data()

    # Call function from app2
    save_results()

    #call function from app2
    monitor_performance()

# Run only if this script is executed directly
if __name__ == "__main__":
    main()
