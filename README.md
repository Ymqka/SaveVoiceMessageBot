Задача:
Разработать Бот ВКонтакте или Телеграмме, сохраняющий аудиосообщения из диалогов в базу данных (СУБД или на диск) по идентификаторам пользователей.

Формат записи: uid —> [audio_message_0, audio_message_1, ..., audio_message_N]
___________________________________________________________________________________________________________________
Вместо добавления в бд самого файла, я сделал добавление пути к этому файлу. Чтобы программа работала нужно узнать токен бота добавить в код токен вашего бота, затем добавить в чат бота и запустить, все голосовые сообщения будут скачиваться в ту же папку, где и скрипт, а затем добавляться в SQLite в виде пути к файлу.
___________________________________________________________________________________________________________________
+ SaveVoice.ipynb - бот
