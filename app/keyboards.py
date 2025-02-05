from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardButton,
                           InlineKeyboardMarkup)


main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
                                     [KeyboardButton(text='Корзина')],
                                     [KeyboardButton(text='Контакты'),
                                      KeyboardButton(text='О нас')]],
                            resize_keyboard=True,
                            input_field_placeholder='Выберите пункт меню...')
catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Футболки')],
                                                [InlineKeyboardButton(text='Кроссовки')],
                                                [InlineKeyboardButton(text='Кепки')]])