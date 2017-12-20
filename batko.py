import config
import telebot
from googletrans import Translator

bot = telebot.TeleBot(config.token)
translator = Translator()


@bot.inline_handler(func=lambda query: True)
def repeat_all_messages(query):
    result = query.query
    try:
        bel_message = translator.translate(query.query, dest='be')
        print(bel_message)
        result = result if bel_message is None else bel_message.text
    except Exception as e:
        print('Could not translate: ' + str(e))

    try:
        r = telebot.types.InlineQueryResultArticle(
            id="1",
            title=result,
            input_message_content=telebot.types.InputTextMessageContent(message_text=result),
        )
        bot.answer_inline_query(query.id, [r], cache_time=5)
    except Exception as e:
        print('Could not answer: ' + str(e))


if __name__ == '__main__':
    bot.polling(none_stop=True)
