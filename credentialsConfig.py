class credConfig:
    def __init__(self, APIKEY = "", DAYS ="", REGION="us-1"):
         self._apikey = APIKEY
         self._days = DAYS
         self._region = REGION

    # getter method
    def get_days(self):
        return self._days
    def get_apikey(self):
        return self._apikey
    def get_region(self):
        return self._region
      
    # setter method
    def set_days(self, x):
        self._days = x
    def set_apikey(self, x):
        self._apikey = x
    def set_region(self, x):
        self._region = x