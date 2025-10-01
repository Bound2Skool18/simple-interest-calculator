def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.

    :param principal: Principal amount (float)
    :param rate: Annual interest rate (percentage, float)
    :param time: Time period in years (float)
    :return: Simple interest (float)
    """
    return (principal * rate * time) / 100

if __name__ == "__main__":
    p = float(input("Enter principal amount: "))
    r = float(input("Enter annual interest rate (%): "))
    t = float(input("Enter time period in years: "))
    si = calculate_simple_interest(p, r, t)
    print(f"Simple Interest = {si}")
