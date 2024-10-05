import discord
import os
from pokemontcgsdk import RestClient, Card
import random
import time

from webserver import keep_alive

client = discord.Client()

api_key = os.environ['api_key']
RestClient.configure(api_key)

shareholders = '@DVA_Online', "@|| Dazza ||", '@The Holy Knight'


class Set :
    def __init__(self, name, amount_of_cards, code) :
        self.name = name
        self.amount_of_cards = amount_of_cards
        self.code = code


swsh_base = Set('Sword and Shield', 216, "swsh1")  # Base
swsh_rbcl = Set('Rebel Clash', 209, "swsh2")  # Rebel Clash
swsh_drka = Set('Darkness Ablaze', 216, "swsh3")  # Darkness Ablaze
swsh_vivo = Set('Vivid Voltage', 203, "swsh4")  # Vivid Voltage
swsh_btst = Set('Battle Styles', 183, "swsh5")  # Battle Styles
swsh_chrn = Set('Chilling Reign', 244, "swsh6")  # Chilling Reign
swsh_evsk = Set('Evolving Skies', 237, "swsh7")  # Evolving Skies
swsh_fnst = Set('Fusion Strike', 284, 'swsh8')  # Fusion Strike
swsh_brst = Set('Brilliant Stars', 186, 'swsh9')  # Brilliant Stars
swsh_asrd = Set('Astral Radiance', 216, 'swsh10')  # Astral Radiance


@client.event
async def on_ready() :
    print('We have logged in as {0.user}'.format(client))
    # name = 'Venusaur V'
    # cards = Card.where(q=f'name:"{name}"', orderBy="set.releaseDate")
    # print(cards[0].images.large)


@client.event
async def on_message(message) :
    channel = message.channel
    if message.author == client.user :
        return

    if message.content.startswith('!hello') :
        await message.channel.send('Hello!')

    if message.content.startswith('!shareholder') :
        await message.channel.send(shareholders)

    if message.content.startswith("!card") :
        await message.channel.send('Set?')

        def check(m) :
            return m.channel == channel

        set = (await client.wait_for('message', check=check)).content

        if set.lower() == 'sword and shield' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if int(card) > swsh_base.amount_of_cards :
                await message.channel.send('https://imgur.com/JYgJFsz')
            else :
                image = f'https://images.pokemontcg.io/{swsh_base.code}/{card}_hires.png'
                await message.channel.send(image)

            card_details = Card.find(f'swsh1-{card}')
            market_price_usd = card_details.cardmarket.prices.averageSellPrice
            card_name = card_details.name

            await message.channel.send(
                f'**{card_name}**   {card}/{swsh_base.amount_of_cards}')
            await message.channel.send(f'Market Price: ${market_price_usd}')

        elif set.lower() == 'rebel clash' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if int(card) > swsh_rbcl.amount_of_cards :
                await message.channel.send('https://imgur.com/JYgJFsz')
            else :
                image = f'https://images.pokemontcg.io/{swsh_rbcl.code}/{card}_hires.png'
                await message.channel.send(image)

            card_details = Card.find(f'swsh2-{card}')
            market_price_usd = card_details.cardmarket.prices.averageSellPrice
            card_name = card_details.name

            await message.channel.send(
                f'**{card_name}**   {card}/{swsh_rbcl.amount_of_cards}')
            await message.channel.send(f'Market Price: ${market_price_usd}')

        elif set.lower() == 'darkness ablaze' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if int(card) > swsh_drka.amount_of_cards :
                await message.channel.send('https://imgur.com/JYgJFsz')
            else :
                image = f'https://images.pokemontcg.io/{swsh_drka.code}/{card}_hires.png'
                await message.channel.send(image)

            card_details = Card.find(f'swsh3-{card}')
            market_price_usd = card_details.cardmarket.prices.averageSellPrice
            card_name = card_details.name

            await message.channel.send(
                f'**{card_name}**   {card}/{swsh_drka.amount_of_cards}')
            await message.channel.send(f'Market Price: ${market_price_usd}')

        elif set.lower() == 'vivid voltage' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if int(card) > swsh_vivo.amount_of_cards :
                await message.channel.send('https://imgur.com/JYgJFsz')
            else :
                image = f'https://images.pokemontcg.io/{swsh_vivo.code}/{card}_hires.png'
                await message.channel.send(image)

            card_details = Card.find(f'swsh4-{card}')
            market_price_usd = card_details.cardmarket.prices.averageSellPrice
            card_name = card_details.name

            await message.channel.send(
                f'**{card_name}**   {card}/{swsh_vivo.amount_of_cards}')
            await message.channel.send(f'Market Price: ${market_price_usd}')

        elif set.lower() == 'battle styles' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if card.isnumeric() :
                if int(card) > swsh_evsk.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh5-{card}')
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')
                await message.channel.send(f'Market Price: ${market_price_usd}')
            else :
                cards = Card.where(q=f'name:"{card}"', orderBy="set.releaseDate")

        elif set.lower() == 'chilling reign' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if card.isnumeric() :
                if int(card) > swsh_evsk.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh6-{card}')
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')
                await message.channel.send(f'Market Price: ${market_price_usd}')
            else :
                cards = Card.where(q=f'name:"{card}"', orderBy="set.releaseDate")

        elif set.lower() == 'evolving skies' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if card.isnumeric() :
                if int(card) > swsh_evsk.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh7-{card}')
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')
                await message.channel.send(f'Market Price: ${market_price_usd}')
            else :
                cards = Card.where(q=f'name:"{card}"', orderBy="set.releaseDate")

                list_length = len(cards)
                i = 0
                while i != list_length :
                    card = cards[i]
                    print(card)
                    await message.channel.send(cards[i].images.large)
                    i += 1

                    # card_details = Card.find(f'{card.set.id}-{card.id}')
                    # market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    # card_name = card_details.name

                    # await message.channel.send(
                    #     f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')

        if set.lower() == 'fusion strike' :
            await message.channel.send('Card no.?')
            card = (await client.wait_for('message', check=check)).content
            if int(card) > swsh_fnst.amount_of_cards :
                await message.channel.send('https://imgur.com/JYgJFsz')
            else :
                image = f'https://images.pokemontcg.io/{swsh_fnst.code}/{card}_hires.png'
                await message.channel.send(image)

            card_details = Card.find(f'swsh8-{card}')
            market_price_usd = card_details.cardmarket.prices.averageSellPrice
            card_name = card_details.name

            await message.channel.send(
                f'**{card_name}**   {card}/{swsh_fnst.amount_of_cards}')
            await message.channel.send(f'Market Price: ${market_price_usd}')

        elif set.lower() == 'brilliant stars' :
            await message.channel.send('Trainer Gallery or Regular?')
            type_card = (await client.wait_for('message', check=check)).content

            if type_card.lower() == 'regular':
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_brst.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_brst.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh9-{card}')
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_brst.amount_of_cards}')
                await message.channel.send(f'Market Price: ${market_price_usd}')

            elif 'trainer' in type_card.lower():
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content

                # using better method
                card_details = Card.find(f'swsh9tg-TG0{card}')
                card_image = card_details.images
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(card_image)
                await message.channel.send(f'**{card_name}**')
                await message.channel.send(f'Market Price: ${market_price_usd}')



        elif set.lower() == 'astral radiance' :
            await message.channel.send('Trainer Gallery or Regular?')
            type_card = (await client.wait_for('message', check=check)).content

            if type_card.lower() == 'regular' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_asrd.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_brst.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh9-{card}')
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_brst.amount_of_cards}')
                await message.channel.send(f'Market Price: ${market_price_usd}')

            elif 'trainer' in type_card.lower() :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content

                # using better method
                card_details = Card.find(f'swsh10tg-TG0{card}')
                card_image = card_details.images
                market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(card_image)
                await message.channel.send(f'**{card_name}**')
                await message.channel.send(f'Market Price: ${market_price_usd}')


    if message.content.startswith("!trade") :
            await message.channel.send("Your offer:")
            await message.channel.send("Set?")

            def check(m) :
                return m.channel == channel

            set = (await client.wait_for('message', check=check)).content

            if set.lower() == 'sword and shield' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_base.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_base.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh1-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_base.amount_of_cards}')

            elif set.lower() == 'rebel clash' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_rbcl.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_rbcl.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh2-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_rbcl.amount_of_cards}')

            elif set.lower() == 'darkness ablaze' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_drka.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_drka.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh3-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_drka.amount_of_cards}')

            elif set.lower() == 'vivid voltage' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_vivo.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_vivo.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh4-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_vivo.amount_of_cards}')

            elif set.lower() == 'battle styles' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if card.isnumeric() :
                    if int(card) > swsh_evsk.amount_of_cards :
                        await message.channel.send('https://imgur.com/JYgJFsz')
                    else :
                        image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                        await message.channel.send(image)

                    card_details = Card.find(f'swsh5-{card}')
                    my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    card_name = card_details.name

                    await message.channel.send(
                        f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')
                else :
                    cards = Card.where(q=f'name:"{card}"', orderBy="set.releaseDate")

            elif set.lower() == 'chilling reign' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if card.isnumeric() :
                    if int(card) > swsh_evsk.amount_of_cards :
                        await message.channel.send('https://imgur.com/JYgJFsz')
                    else :
                        image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                        await message.channel.send(image)

                    card_details = Card.find(f'swsh6-{card}')
                    my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    card_name = card_details.name

                    await message.channel.send(
                        f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')
                else :
                    cards = Card.where(q=f'name:"{card}"', orderBy="set.releaseDate")

            elif set.lower() == 'evolving skies' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if card.isnumeric() :
                    if int(card) > swsh_evsk.amount_of_cards :
                        await message.channel.send('https://imgur.com/JYgJFsz')
                    else :
                        image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                        await message.channel.send(image)

                    card_details = Card.find(f'swsh7-{card}')
                    my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    card_name = card_details.name

                    await message.channel.send(
                        f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')
                else :
                    cards = Card.where(q=f'name:"{card}"', orderBy="set.releaseDate")

            if set.lower() == 'fusion strike' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_fnst.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_fnst.code}/{card}_hires.png'
                    await message.channel.send(image)
                card_details = Card.find(f'swsh8-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_fnst.amount_of_cards}')

            elif set.lower() == 'brilliant stars' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_brst.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_brst.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh9-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_brst.amount_of_cards}')

            elif set.lower() == 'astral radiance' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_asrd.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_asrd.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh10-{card}')
                my_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_asrd.amount_of_cards}')

            await message.channel.send('Their offer:')
            await message.channel.send("Set?")

            def check(m) :
                return m.channel == channel

            set = (await client.wait_for('message', check=check)).content

            if set.lower() == 'sword and shield' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_base.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_base.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh1-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_base.amount_of_cards}')

            elif set.lower() == 'rebel clash' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_rbcl.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_rbcl.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh2-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_rbcl.amount_of_cards}')

            elif set.lower() == 'darkness ablaze' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_drka.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_drka.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh3-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_drka.amount_of_cards}')

            elif set.lower() == 'vivid voltage' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_vivo.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_vivo.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh4-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_vivo.amount_of_cards}')

            elif set.lower() == 'battle styles' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if card.isnumeric() :
                    if int(card) > swsh_evsk.amount_of_cards :
                        await message.channel.send('https://imgur.com/JYgJFsz')
                    else :
                        image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                        await message.channel.send(image)

                    card_details = Card.find(f'swsh5-{card}')
                    their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    card_name = card_details.name

                    await message.channel.send(
                        f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')

            elif set.lower() == 'chilling reign' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if card.isnumeric() :
                    if int(card) > swsh_evsk.amount_of_cards :
                        await message.channel.send('https://imgur.com/JYgJFsz')
                    else :
                        image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                        await message.channel.send(image)

                    card_details = Card.find(f'swsh6-{card}')
                    their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    card_name = card_details.name

                    await message.channel.send(
                        f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')

            elif set.lower() == 'evolving skies' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if card.isnumeric() :
                    if int(card) > swsh_evsk.amount_of_cards :
                        await message.channel.send('https://imgur.com/JYgJFsz')
                    else :
                        image = f'https://images.pokemontcg.io/{swsh_evsk.code}/{card}_hires.png'
                        await message.channel.send(image)

                    card_details = Card.find(f'swsh7-{card}')
                    their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                    card_name = card_details.name

                    await message.channel.send(
                        f'**{card_name}**   {card}/{swsh_evsk.amount_of_cards}')

            if set.lower() == 'fusion strike' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_fnst.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_fnst.code}/{card}_hires.png'
                    await message.channel.send(image)
                card_details = Card.find(f'swsh8-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_fnst.amount_of_cards}')

            elif set.lower() == 'brilliant stars' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_brst.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_brst.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh9-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_brst.amount_of_cards}')

            elif set.lower() == 'astral radiance' :
                await message.channel.send('Card no.?')
                card = (await client.wait_for('message', check=check)).content
                if int(card) > swsh_asrd.amount_of_cards :
                    await message.channel.send('https://imgur.com/JYgJFsz')
                else :
                    image = f'https://images.pokemontcg.io/{swsh_asrd.code}/{card}_hires.png'
                    await message.channel.send(image)

                card_details = Card.find(f'swsh10-{card}')
                their_market_price_usd = card_details.cardmarket.prices.averageSellPrice
                card_name = card_details.name

                await message.channel.send(
                    f'**{card_name}**   {card}/{swsh_asrd.amount_of_cards}')

            await message.channel.send(
                f'\nYour offer is worth: ${my_market_price_usd}\nTheir offer is worth: ${their_market_price_usd}')
            if my_market_price_usd > their_market_price_usd :
                loss = my_market_price_usd - their_market_price_usd
                await message.channel.send(f'Trade: You are losing ${round(loss, 2)} in USD')
            elif my_market_price_usd < their_market_price_usd :
                profit = their_market_price_usd - my_market_price_usd
                await message.channel.send(f'Trade: You are profiting ${round(profit, 2)} in USD')
            else :
                await message.channel.send('Trade: You are not losing nor profiting')

    if message.content.startswith("!higherlower") :
        count = 0
        for i in range(10) :
            rand_set = random.randint(1, 10)
            if rand_set == 1 :
                rand_card = random.randint(1, swsh_base.amount_of_cards)
            elif rand_set == 2 :
                rand_card = random.randint(1, swsh_rbcl.amount_of_cards)
            elif rand_set == 3 :
                rand_card = random.randint(1, swsh_drka.amount_of_cards)
            elif rand_set == 4 :
                rand_card = random.randint(1, swsh_vivo.amount_of_cards)
            elif rand_set == 5 :
                rand_card = random.randint(1, swsh_btst.amount_of_cards)
            elif rand_set == 6 :
                rand_card = random.randint(1, swsh_chrn.amount_of_cards)
            elif rand_set == 7 :
                rand_card = random.randint(1, swsh_evsk.amount_of_cards)
            elif rand_set == 8 :
                rand_card = random.randint(1, swsh_fnst.amount_of_cards)
            elif rand_set == 9 :
                rand_card = random.randint(1, swsh_brst.amount_of_cards)
            elif rand_set == 10 :
                rand_card = random.randint(1, swsh_asrd.amount_of_cards)

            await message.channel.send(f"https://images.pokemontcg.io/swsh{rand_set}/{rand_card}_hires.png")

            card_details1 = Card.find(f'swsh{rand_set}-{rand_card}')
            first_card = card_details1.cardmarket.prices.averageSellPrice
            card_name1 = card_details1.name
            await message.channel.send(f'{card_name1} | ${first_card}')

            rand_set2 = random.randint(1, 10)

            if rand_set2 == 1 :
                rand_card = random.randint(1, swsh_base.amount_of_cards)
            elif rand_set2 == 2 :
                rand_card = random.randint(1, swsh_rbcl.amount_of_cards)
            elif rand_set2 == 3 :
                rand_card = random.randint(1, swsh_drka.amount_of_cards)
            elif rand_set2 == 4 :
                rand_card = random.randint(1, swsh_vivo.amount_of_cards)
            elif rand_set2 == 5 :
                rand_card = random.randint(1, swsh_btst.amount_of_cards)
            elif rand_set2 == 6 :
                rand_card = random.randint(1, swsh_chrn.amount_of_cards)
            elif rand_set2 == 7 :
                rand_card = random.randint(1, swsh_evsk.amount_of_cards)
            elif rand_set2 == 8 :
                rand_card = random.randint(1, swsh_fnst.amount_of_cards)
            elif rand_set2 == 9 :
                rand_card = random.randint(1, swsh_brst.amount_of_cards)
            elif rand_set2 == 10 :
                rand_card = random.randint(1, swsh_asrd.amount_of_cards)

            rand_card2 = random.randint(1, 183)
            await message.channel.send(f"https://images.pokemontcg.io/swsh{rand_set2}/{rand_card2}_hires.png")

            card_details2 = Card.find(f'swsh{rand_set2}-{rand_card2}')
            second_card = card_details2.cardmarket.prices.averageSellPrice
            card_name2 = card_details2.name

            await message.channel.send("Higher or Lower?")

            def check(m) :
                return m.channel == channel

            guess = (await client.wait_for('message', check=check)).content

            if guess.lower() == 'higher' :
                if second_card > first_card :
                    await message.channel.send(f'Correct! {card_name2} is priced at ${second_card}')
                    count += 1
                    time.sleep(1)
                elif second_card < first_card :
                    await message.channel.send(f'Incorrect! {card_name2} is priced at ${second_card}')
                    count += 1
                    time.sleep(1)

                    if count <= 3 :
                        await message.channel.send(f'You got through {count} rounds. You can do better...')
                    elif 3 < count > 8 :
                        await message.channel.send(f'You got through {count} rounds. Well done!')
                    elif count >= 8 :
                        await message.channel.send(f'You got through {count} rounds. Wow, great job!')

                    break
                else :
                    await message.channel.send('They are both priced the same!')
            elif guess.lower() == 'lower' :
                if second_card < first_card :
                    await message.channel.send(f'Correct! {card_name2} is priced at ${second_card}')
                    count += 1
                    time.sleep(1)
                elif second_card > first_card :
                    await message.channel.send(f'Incorrect! {card_name2} is priced at ${second_card}')
                    count += 1
                    time.sleep(1)

                    if count <= 3 :
                        await message.channel.send(f'You got through {count} rounds. You can do better...')
                    elif 3 < count > 8 :
                        await message.channel.send(f'You got through {count} rounds. Well done!')
                    elif count >= 8 :
                        await message.channel.send(f'You got through {count} rounds. Wow, great job!')

                    break
                else :
                    await message.channel.send('They are both priced the same!')
                    time.sleep(1)

            elif guess.lower() == 'stop':

                await message.channel.send(f'You got through {count} rounds.')
                await message.channel.send('Thanks for playing!')
                break

    # https://images.pokemontcg.io/swsh7/167_hires.pn


keep_alive()
my_secret = os.environ['TOKEN']
client.run(my_secret)
