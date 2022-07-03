#!/usr/bin/python3

'''class Review'''

import models


class Review(models.base_model.BaseModel):
    '''defining review'''
    place_id = ""
    user_id = ""
    text = ""
