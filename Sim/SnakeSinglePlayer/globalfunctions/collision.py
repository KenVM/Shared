from kivy.uix.widget import Widget

def collision(widget1, widget2):
    #compare if the block collides with one of the blocks of the list
    #should be a block and a list, order does not metter
    collision_detected = False

    if isinstance(widget1, list) and not isinstance(widget2, list):
        for blok in widget1[:]:
            if widget2.collide_widget(blok) == True:
                collision_detected = True

    if isinstance(widget2, list) and not isinstance(widget1, list):
        for blok in widget2[:]:
            if widget1.collide_widget(blok) == True:
                collision_detected = True


    return collision_detected
