"""Controller for speaking with robot"""
from AppRobot.roboter.models import robot
from AppRobot.roboter.models.robot import RestaurantRobot


def talk_about_restaurant():
    """Function to speak with robot"""
    restaurant_robot: RestaurantRobot = robot.RestaurantRobot()
    restaurant_robot.hello()
    restaurant_robot.recommend_restaurant()
    restaurant_robot.ask_user_favorite()
    restaurant_robot.thank_you()

