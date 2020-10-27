import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='')
()
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hi {ctx.author.mention} Bro')

@bot.command()
async def what(ctx):
    await ctx.send('Teri to.... :) ')

@bot.command()
async def wt(ctx):
    await ctx.send(' :) ')

@bot.command()
async def lol(ctx):
    await ctx.send(' hahahaha ')

@bot.command()
async def gm(ctx):
    await ctx.send(f' GoodMorning {ctx.author.mention} Bhai ')

@bot.command()
async def gn(ctx):
    await ctx.send(' GoodNight Bhai ')

@bot.command()
async def whatareyoudoing(ctx):
    await ctx.send(' Waiting for your commands ')

@bot.command()
async def whatisyourname(ctx):
    await ctx.send(' Andhe mera naam likha hua hai dekh nahi sakta kya :-) ')

@bot.command()
async def sorry(ctx):
    await ctx.send(' Its ok just chill, and have fun :-) ')

@bot.command()
async def encorageme(ctx):
    await ctx.send(' You can do anything Just go  and do what ever you can u are expert in that thing u want to do Best of luck for the work ')

@bot.command()
async def wiyc(ctx):
    await ctx.send(' Dogdev is my c he os very moob :-) oh moo he will kill me ')

@bot.command()
async def cool(ctx):
	await ctx.send(f'Wow!this is really so cool! {ctx.author.mention}')

@bot.command()
async def Salaam(ctx):
	await ctx.send(f'Salaam {ctx.author.mention} Bhai')
	
@bot.command()
async def bye(ctx):
	await ctx.send(f'Bye Bye ^_^ {ctx.author.mention} ')

#some more		

@bot.command()
async def rjk(ctx):
	await ctx.send('I dont remember Jokes')
	
@bot.command()
async def ashameme(ctx):
	await ctx.send(f'You cant do anything bcoz you are a noob {ctx.author.mention} You are very ugly :-(')
	
@bot.command()
async def sas(ctx):
	await ctx.send(f':-( :-( for {ctx.author.mention} ')

#moo commamds

@bot.command()
async def moo(ctx):
	await ctx.send('@Moo iss bhikari ki baat sunle ')

@bot.command()
async def sorrymoo(ctx):
	await ctx.send(f'Sorry moo me{ctx.author.mention} ki taraf se mafi manga ta hun')

@bot.command()
async def thnxmoo(ctx):
	await ctx.send('Are Wah! Moo tu toh kamal hai! :-) ')



client.run(os.getenv('Token'))
