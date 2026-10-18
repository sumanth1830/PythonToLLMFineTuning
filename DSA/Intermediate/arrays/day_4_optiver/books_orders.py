# LeetCode 1803

from collections import deque, defaultdict


class Order:
    def __init__(self, price, amount, order_type):
        self.price = price
        self.qty = amount
        self.order_type = order_type


class Solution(object):
    def getNumberOfBacklogOrders(self, orders):
        """
        :type orders: List[List[int]]
        :rtype: int
        """
        buys = defaultdict(deque)
        sells = defaultdict(deque)

        for order in orders:
            if order[-1] == 0:
                # Buy order, look for sells
                order = Order(order[0], order[1], "BUY")
                while order.qty > 0 and sells and order.price >= min(sells):
                    best = min(sells)
                    resting = sells[best][0]
                    traded = min(order.qty, resting.qty)
                    order.qty -= traded
                    resting.qty -= traded
                    if resting.qty == 0:
                        sells[best].popleft()
                        if not sells[best]:
                            del sells[best]

                if order.qty > 0:
                    buys[order.price].append(order)

            elif order[-1] == 1:
                order = Order(order[0], order[1], "SELL")
                while order.qty > 0 and buys and order.price <= max(buys):
                    best = max(buys)
                    resting = buys[best][0]
                    traded = min(order.qty, resting.qty)
                    order.qty -= traded
                    resting.qty -= traded
                    if resting.qty == 0:
                        buys[best].popleft()
                        if not buys[best]:
                            del buys[best]

                if order.qty > 0:
                    sells[order.price].append(order)

        # print(buys)
        # print(sells)

        total = 0
        for queue in list(buys.values()) + list(sells.values()):
            total += sum(o.qty for o in queue)

        return total % 1000000007


# orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
# Output = 6
# Explanation: Here is what happens with the orders:
# - 5 orders of type buy with price 10 are placed.
#   There are no sell orders, so the 5 orders are added to the backlog.
# - 2 orders of type sell with price 15 are placed.
#   There are no buy orders with prices larger than or equal to 15,
#       so the 2 orders are added to the backlog.
# - 1 order of type sell with price 25 is placed.
#   There are no buy orders with prices larger than or equal to 25 in the backlog,
#   so this order is added to the backlog.
# - 4 orders of type buy with price 30 are placed.
#   The first 2 orders are matched with the 2 sell orders of the least price,
#   which is 15 and these 2 sell orders are removed from the backlog.
#   The 3rd order is matched with the sell order of the least price,
#   which is 25 and this sell order is removed from the backlog.
#   Then, there are no more sell orders in the backlog, so the 4th order is added to the backlog.
# Finally, the backlog has 5 buy orders with price 10, and 1 buy order with price 30.
# So the total number of orders in the backlog is 6.
