def calculate_discount(order_time):
    # Convert order time to 24-hour format for easier comparison
    order_time = order_time.strip().lower()
    if order_time.endswith('pm') and order_time != '12pm':
        order_time = str(int(order_time.split(':')[0]) + 12) + order_time[order_time.find(':'):]
    elif order_time.endswith('am') and order_time.startswith('12'):
        order_time = '00' + order_time[2:]

    # Remove 'am' or 'pm' for comparison
    order_time = order_time.replace('am', '').replace('pm', '')
    
    # Convert string time to integer minutes
    hours, minutes = map(int, order_time.split(':'))
    total_minutes = hours * 60 + minutes

    # Define discount time ranges in minutes
    discount_start_morning = 3 * 60  # 3 AM in minutes
    discount_end_morning = 15 * 60   # 3 PM in minutes
    discount_start_evening = 18 * 60  # 6 PM in minutes
    discount_end_evening = 21 * 60    # 9 PM in minutes

    # Check if the order time is within the discount time range
    if (total_minutes < discount_end_morning and total_minutes >= discount_start_morning) or \
       (total_minutes < discount_end_evening and total_minutes >= discount_start_evening):
        return "Customer gets a 15% discount."
    else:
        return "No discount available."

# Example usage:
print(calculate_discount('2:45 pm'))  # Customer gets a 15% discount.
print(calculate_discount('5:00 pm'))  # No discount available.
print(calculate_discount('7:30 pm'))  # Customer gets a 15% discount.