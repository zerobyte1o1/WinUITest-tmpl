from pageObject.home_page import HomePage


class HomeHandler(HomePage):

    def click_mals_procing_loc(self):
        self.get_mals_procing_loc().left_click()



if __name__ == '__main__':
    HomeHandler().click_mals_procing_loc()