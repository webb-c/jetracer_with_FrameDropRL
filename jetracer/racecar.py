import traitlets


class Racecar(traitlets.HasTraits):
    steering = traitlets.Float()
    throttle = traitlets.Float()
    gainUp = traitlets.Float()
    gainDown = traitlets.Float()
    
    @traitlets.validate('steering')
    def _clip_steering(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']
        
    @traitlets.validate('throttle')
    def _clip_throttle(self, proposal):
        if proposal['value'] > 1.0:
            return 1.0
        elif proposal['value'] < -1.0:
            return -1.0
        else:
            return proposal['value']
        
#     @traitlets.validate('gainUp')
#     def _clip_gainUp(self, proposal):
#         if proposal['value'] > 1.0:
#             return 1.0
#         elif proposal['value'] < 0.0:
#             return 0.0
#         else:
#             return proposal['value']
        
#     @traitlets.validate('gainDown')
#     def _clip_gainDown(self, proposal):
#         if proposal['value'] > 1.0:
#             return 1.0
#         elif proposal['value'] < 0.0:
#             return 0.0
#         else:
#             return proposal['value']