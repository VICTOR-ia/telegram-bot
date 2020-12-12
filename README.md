# Телеграм Бот

## Описание идеи
Цель проекта состоит в написании телеграм бота, который позволит следить за постами выбранных пабликов (через [VK API](https://vk.com/dev/wall.get))

## Принцип работы
Бот реагирует на определенные команды:
- /subscribe `ID паблика`
- /unsubscribe `ID паблика`
- /subscriptions

Но для удобства были созданы соответсвующие кнопки.
![Кнопки](https://sun9-3.userapi.com/impf/efP5snkN5QdKBOJSM1uwsuSKUPDp9T78WUZnLQ/qyf38NEpc9Y.jpg?size=650x138&quality=96&proxy=1&sign=7c8886ffd15b4f4dc77b80365758e41e&type=album)

Для каждой из команд добавляется соответсвующий обработчик:
![Обработчик команд](https://sun9-76.userapi.com/impf/Vdpqjk3aiX_eO0zZZAHz8VCnPLGmH6uatcQPWA/LY7e8DuV48Q.jpg?size=791x338&quality=96&proxy=1&sign=a532491b0e7fcf8ae7949c71f9bd1647&type=album)

### Обработчики команд
`subscribe.py`:
1. Обработчик получает `ID паблика`, переданного пользователем
2. Делается запрос через [VK API](https://vk.com/dev/wall.get)
3. Сохраняется `ID` последнего поста, чтобы в дальнейшей сравнивать с предыдущим (это будет сигналом того, что вышел новый пост)
4. При несовпадении `ID` текущего и последнего постов - бот высылает сообщение с новым постом.

![Подписка оформлена](https://sun9-17.userapi.com/impf/NcnGfmuZa0pbh7dUdOSGdGfOPz6Ivb2RHLj56g/NhgXRZ-GHoU.jpg?size=648x143&quality=96&proxy=1&sign=b681797dd31949b883ea3fae37ad23dd&type=album)
![Новый пост](https://sun9-33.userapi.com/impf/yiaq8mOMTuyOQu8W-n04kMB1kPd314YmEuFFSw/WfzEk0aEoK4.jpg?size=648x694&quality=96&proxy=1&sign=cb8ae3ed875029b2743e6a435c6891fa&type=album)

`unsubscribe.py`:
1. Обработчик получает `ID паблика`, переданного пользователем
2. Если `ID паблика` есть в текущем списке подписок, то подписка отменяется - поток запросов приостанавливается 

![Подписка отменена](https://sun9-34.userapi.com/impf/nkcsWDRdZxCFS068kcosXXYE19SHSsSOytOY_Q/llCfAKxgzoI.jpg?size=643x186&quality=96&proxy=1&sign=b5b7519434d1ee1cef358b4e823941b5&type=album)

`subscriptions.py`:
1. Если список подписок не пуст, то отправляется список текущих подписок, иначе - сообщение о том, что список пуст

![Список подписок](https://sun9-49.userapi.com/impf/ah8UXTfkwSthX0qha2DC7nM0kRIbwWNfkaituw/cLtNbSJUvrI.jpg?size=649x209&quality=96&proxy=1&sign=261c7e6371fa359cef74171bc6438926&type=album)
![Список пуст](https://sun9-59.userapi.com/impf/6H2HQh8CaE7nV0Z7slxkJ8IBkubyiyPho-z_Jg/0LehP_Ln2jk.jpg?size=648x86&quality=96&proxy=1&sign=c1e3e85bbce1272e491ce0d0326b33df&type=album)
