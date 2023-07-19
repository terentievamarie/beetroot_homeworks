class TVController:
    def __init__(self,channels):
        self.channels=channels
        self.channel_index=0

    def first_channel(self):
        print(self.channels[0])
    
    def last_channel(self):
        print(self.channels[-1])
    
    def turn_channel(self,N):
        if 1<=N<=len(self.channels):
            return self.channels[N-1]
        return "Please,try again"
    
    def next_channel(self):
        self.channel_index = (self.channel_index + 1) % len(self.channels)
        return self.channels[self.channel_index]
    
    def previos_channel(self):
        self.channel_index=(self.channel_index-1)% len(self.channels)
        return self.channels[self.channel_index]
    
    def current_channel(self):
        return self.channels[self.channel_index]
    
    def is_exist(self,channel):
        if isinstance(channel,int):
            if 1<=channel<=len(self.channels):
                return 'Yes'
            return 'No'
        elif isinstance(channel,str):
            if channel in self.channels:
                return 'Yes'
            return 'No'
        else:
            return "Your input is incorrect"
        
tv_controller_1=TVController(["BBC", "Discovery", "TV1000"])
tv_controller_1.first_channel()
tv_controller_1.last_channel()
print(tv_controller_1.turn_channel(2))
print(tv_controller_1.next_channel())
print(tv_controller_1.previos_channel())
print(tv_controller_1.current_channel())
print(tv_controller_1.is_exist("Discovery"))

            
        
            


    
