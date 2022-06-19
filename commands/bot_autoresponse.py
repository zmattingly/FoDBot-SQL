from .common import *

# Load up our list of complimentary adjectives
with open('bot_affirmations.txt') as f:
  bot_affirmations = f.read().splitlines() 

# bot_affirmations(message) - responds to bot compliments
# message[required]: discord.Message
async def handle_bot_affirmations(message:discord.Message):
  for affirmation in bot_affirmations:
    if f"{affirmation} bot" in message.content.lower():
      logger.info(f"The Bot received some {Fore.RED}love{Fore.RESET} from {Fore.LIGHTBLUE_EX}{message.author.display_name}{Fore.RESET}")
      await message.add_reaction(EMOJI["love"])
      await message.reply(random.choice(config["bot_responses"]), mention_author=True)
      break