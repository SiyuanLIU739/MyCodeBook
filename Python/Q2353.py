import heapq

class Food:
    def __init__(self, food, rating, cuisine):
        self.food = food
        self.rating = rating
        self.cuisine = cuisine
    
    def __lt__(self, other):
        return self.rating > other.rating

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.menu = {}
        self.foodbook = {}

        for i in range(len(foods)):
            foodname = foods[i]
            cuisine = cuisines[i]
            rating = ratings[i]

            food = Food(foodname, rating, cuisine)
            self.foodbook[foodname] = food

            lst = []
            if(cuisine in self.menu.keys()):
                lst = self.menu[cuisine]
            heapq.heappush(lst, food)
            self.menu[cuisine] = lst


    def changeRating(self, food: str, newRating: int) -> None:
        foodobj = self.foodbook[food]
        cuisine = foodobj.cuisine
        foodobj = Food(food, newRating, cuisine)

        lst = self.menu[cuisine]
        heapq.heappush(lst, foodobj)

        self.foodbook[food] = foodobj

    def highestRated(self, cuisine: str) -> str:
        lst = self.menu[cuisine]
        
        top = lst[0]
        while(top.rating != self.foodbook[top.food].rating):
            heapq.heappop(lst)
            top = lst[0]

        return top.food