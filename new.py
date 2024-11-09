def check_discount(order_time):
    """
    Checks if the customer is eligible for a 15% discount based on the order time.
    
    Parameters:
    order_time (str): The time the order is placed in the format "HH:MM".
    
    Returns:
    str: Message indicating whether the customer gets a discount or not.
    """
    # Convert the order time into hours and minutes
    hour, minute = map(int, order_time.split(":"))
    
    # Define the discount periods
    before_3pm = (hour < 15)
    after_6pm_before_9pm = (18 <= hour < 21)
    
    # Check if the order time is within the discount periods
    if before_3pm or after_6pm_before_9pm:
        return "Customer gets a 15% discount."
    else:
        return "Customer does not get a discount."

# Example usage:
order_time1 = "14:30"
order_time2 = "19:45"
order_time3 = "15:30"

print(f"Order time {order_time1}: {check_discount(order_time1)}")
print(f"Order time {order_time2}: {check_discount(order_time2)}")
print(f"Order time {order_time3}: {check_discount(order_time3)}")