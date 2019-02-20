import discord, time, datetime
from discord.ext import commands
from discord.ext.commands import Bot
from discord.voice_client import VoiceClient
from discord.utils import get
import asyncio
import time
import colorsys
import sys
import subprocess
import os
import json
import traceback
import random
from random import choice
import request


start_time = time.time()


bot = commands.Bot('ls!')
bot.remove_command('help')
print (discord.__version__)
COLOUR = 0xFFFF00
COR = 0x00ff00


@bot.event
async def on_ready():
	global id
	id = "TETEU 147"
	while True:
		await bot.change_presence(game=discord.Game(name='Bot Oficial Da Legend•Squad hehe'))
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='Marque Seu Teste!'))
		await asyncio.sleep(20)
		await asyncio.sleep(20)
		await bot.change_presence(game=discord.Game(name='para ' + str(len(set(bot.get_all_members())))+ ' Legends!👥', type=1))
		await asyncio.sleep(20)		
		

@bot.event
async def on_member_join(member):
	emoji = get(bot.get_all_emojis(), name='PinguWithGun')
	pessoa = member.name
	canal = bot.get_channel("547568615776583694")
	regras = bot.get_channel("547563502731264010")
	registro = bot.get_channel("547553709324894220")
	msg = discord.Embed(title='Um Novo Membro No Servidor!', description="{} Seja bem vindo ao **Legend•Squad** Leia as {} e va em {} para marcar seu teste! {}".format(member.mention, regras.mention, registro.mention, emoji), color=0x00ff00)
	msg.set_author(name=pessoa, icon_url=member.avatar_url)
	msg.set_footer(text='Bot Oficial Da Legend | Fui criado pelo TETEU 147')
	await bot.send_message(canal, embed=msg) 
	




	
@bot.event
async def on_member_remove(member):
   canal = bot.get_channel("547568729584566302")
   emoji = get(bot.get_all_emojis(), name='hioubye')
   pessoa = member.name
   msg = discord.Embed(title='Um Membro Saiu Do Servidor', description="{} Saiu Do Servidor. Espero Que Um Dia Ele Volte! {}".format(member.mention, emoji), color=0xff0000)
   msg.set_author(name=pessoa, icon_url=member.avatar_url)
   msg.set_footer(text='Bot Oficial Da Legend | Fui criado pelo TETEU 147')
   await bot.send_message(canal, embed=msg) 

@bot.command(pass_context=True)
async def suicidio(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533344634576044052/tumblr_nee9xjzaxR1r3rdh2o1_500-1.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/533344635247001602/47892bb88afc132a3afb775988208240.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Suicidio 💔',  description='**{}** se suicidou!'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, motivo: str = None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``ls!ban <@usuário> <motivo>``')
	else:
		await bot.ban(member)
		embed = discord.Embed(title='usuário banido!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário banido', value=member.name)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando realizado por {} | legend•Squad Oficial'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você foi banido!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que foi banido', value=ctx.message.server.name)
		embedpv.add_field(name='Motivo', value=motivo)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(member, embed=embedpv)
		print('comando ban digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
							
@bot.command(pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.User, *, motivo: str = None):
	if not motivo:
		return await bot.say('Você não especificou o motivo. Exemplo: ``ls!kick <@usuário> <motivo>``')
	else:
		await bot.kick(user)
		embed = discord.Embed(title='usuário expulso!', description='{} usuário banido com sucesso'.format(ctx.message.author.mention), color=0xff0Ab)
		embed.add_field(name='Autor', value=ctx.message.author)
		embed.add_field(name='usuário banido', value=user.name)
		embed.add_field(name='Motivo', value=motivo)
		embed.set_footer(text='Comando realizado por {} | Legend•Squad Oficial'.format(ctx.message.author.name))
		await bot.say(embed=embed)
		embedpv = discord.Embed(title='Você foi expulso!'.format(ctx.message.author.mention), color=0xff0Ab)
		embedpv.add_field(name='Autor', value=ctx.message.author)
		embedpv.add_field(name='servidor em que foi expulso', value=ctx.message.server.name)
		embedpv.add_field(name='Motivo', value=motivo)
		embedpv.set_thumbnail(url=ctx.message.server.icon_url)
		await bot.send_message(user, embed=embedpv)
	print('comando kick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
		
@bot.command(pass_context=True)
async def matar(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/539733424185802762/b19b70f5c546ec7c67c2f0b4e61c21f743a5acaf_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539733902097645568/tumblr_m6rerquar01qd4f2uo1_500.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Assasino!',  description='👮☎| **{}** Matou **{}**! ASSASINO!'.format(ctx.message.author.name, user.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
		
@bot.command(pass_context=True)
async def votar(ctx, *, mensagem: str= None):
	if not mensagem:
		return await bot.say('Você precisa falar algo para votar')
	else:
			vote = await bot.say(embed=discord.Embed(color=0xff0000, description=mensagem))
			await bot.add_reaction(vote, "✅")
			await bot.add_reaction(vote, "❌")
	print('comando votar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def kiss(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/533253217883258890/tumblr_mie2frAdXc1rfj82jo2_500.gif','https://cdn.discordapp.com/attachments/514045065929162764/533253218860269577/86d4a046c8a32a28341353fc95bedc82.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494353694097438/feliz-aniversario-6224237-140820161718.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Beijo! ❤',  description='**{}** recebeu um beijo de **{}**! Casal Fofo! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando kiss digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
@bot.command(pass_context=True)
async def hug(ctx, user: discord.User):
	list = 'https://cdn.discordapp.com/attachments/531090629715951629/532667673943736351/action.gif','https://cdn.discordapp.com/attachments/531090629715951629/532672938596368393/action.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/539494351555002379/tumblr_mdi1l8AaDi1rcm8d4o1_500.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Abraço ❤',  description='**{}** Ele(a) recebeu um abraço de **{}**!! :heart_eyes:'.format(user.name, ctx.message.author.name), color=0x00ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	
@bot.command(pass_context=True)
async def kepiada(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589504/Piada_mulher_de_tpm_cafe.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589505/images_6.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537245589506/images_4.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758537711026177/o_rapaz_apaixonado_diz_a_sua_amada.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604810/images_5.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538214604812/ladrao-em-casa-3684XBr1G1DBAQ.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567424/Passa_Passa_Passa.jpg', 'https://cdn.discordapp.com/attachments/514045065929162764/539758538734567425/na_delegacia_seu_delegado_meu_marido_saiu_de_casa.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='Piadas', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Favelada Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando kepiada digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
@bot.command(pass_context=True)
async def report(ctx, user: discord.User, *, motiv: str=None, limit: int=1):
	if not motiv:
		return await bot.say('Você Não especificou motivo do reporte')
	async for msg in bot.logs_from(ctx.message.channel, limit=1):
            try:
                await bot.delete_message (msg)
            except:
                pass
                embed = discord.Embed(title="usuário reportado", description="seu reporte foi enviado com sucesso! caso for aprovado o usuário reportado sera punido".format(ctx.message.author.mention), color=0x00ff00)

                await asyncio.sleep(2)
	canal = bot.get_channel("547725354576642049")
	horario = datetime.datetime.now().strftime("%H:%M:%S")	
	ms = discord.Embed(title='usuário reportado', color=0x00ff00)
	
	ms.add_field(name="Autor", value=ctx.message.author.name, inline=True)
	ms.add_field(name="usuário reportado", value=user, inline=True)
	ms.add_field(name="Hora", value=horario, inline=True)
	ms.add_field(name="Motivo", value=motiv, inline=True)
	await bot.send_message(canal, embed=ms)
	await bot.say(embed=embed)			



@bot.command(pass_context=True)
async def meme(ctx):
	a = 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349760/images_9.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763086895349761/cara-mano-tatuei-o-nome-da-minha-namora-e-ela-20426746.png', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032640/images_7.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763087474032641/images_10.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088002383883/images_11.jpeg', 'https://cdn.discordapp.com/attachments/514045065929162764/539763088455630855/3d6dcd431d328b82ac2bc8edf5f754ee--kawaii.jpg'
	hug = random.choice(a)
	hugemb = discord.Embed(title='SO MEME DE QUALIDADE MONSTRA', color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando meme digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

	

	
@bot.command(pass_context = True)
@commands.has_permissions(manage_nicknames=True)     
async def setnick(ctx, user: discord.Member, *, nickname):
    await bot.change_nickname(user, nickname)
    emb = discord.Embed(title='Apelido alterado')
    emb.add_field(name='usuário', value =user.name)
    emb.add_field(name='Autor', value =ctx.message.author.name)
    await bot.say(embed=emb)
    print('comando setnick digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
    


	
@bot.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.add_roles(member, role)
    embed = discord.Embed(description=' ✅Role Adicionada com sucesso!', color=0x00ff00)
    await bot.say(embed=embed)
    print('comando addrole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
  
@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def avisar(ctx, member: discord.Member, *, content: str):
	embed = discord.Embed(description='{} foi avisado com sucesso! por {}'.format(member.mention, ctx.message.author.mention), color=0x7a00bb)
	embedpv = discord.Embed(title='Aviso', color=0x00AB70)
	embedpv.add_field(name='Aviso Do servidor', value=ctx.message.server.name)
	embedpv.add_field(name='Autor', value=ctx.message.author)
	embedpv.add_field(name='Motivo', value=content)
	embedpv.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.send_message(member, embed=embedpv)
	
	await bot.say(embed=embed)  
	print('comando avisar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))	 
    
          
@bot.command(pass_context=True)
async def falar(ctx, *, arg):
	await bot.say(arg)
	print('comando falar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await bot.send_typing(channel)
	t2 = time.perf_counter()
	embed=discord.Embed(title="Pong!", description='Meu Ping {}ms.'.format(round((t2-t1)*1000)), color=0x76FF03)
	embed.set_footer(text ='comando realizado por {}| Bot Oficial Legend•Squad'.format(ctx.message.author.name))
	await bot.say(embed=embed)

@bot.command(pass_context=True)
@commands.has_permissions(gerence_res=True)
async def removerole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await bot.remove_roles(member, role)
    embed = discord.Embed(description=' 👮Role removida com sucesso', color=0xff0000)
    await bot.say(embed=embed)
    print('comando removerole digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
	
			
@bot.command(pass_context=True)
async def diversaoajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.add_field(name = 'ls!kiss ',value ='Como usar ``ls!kiss @usuário`` O amor esta no ar! beije determinado usuário!',inline = False)
    embed.add_field(name = 'ls!hug ',value ='Como usar ``s!abraçar @usuário`` abrace seu/sua melhor amigo(a).',inline = False)
    embed.add_field(name = 'ls!avatar ',value ='Como usar ``ls!avatar @usuário`` Veja o avatar do usuário',inline = False)
    embed.add_field(name="ls!meme", value="como usar ``ls!meme`` que tal ver alguns memes?!", inline=False)
    embed.add_field(name="ls!ping", value="como usar ``ls!ping`` Veja meu tempo de resposta!", inline=False)
    embed.add_field(name="ls!userinfo", value="como usar ``ls!userinfo @usuário`` Veja o perfil de um determinado usuário!", inline=True)
    embed.add_field(name="ls!kepiada", value="como usar ``ls!kepiada`` piadas engraçadas!", inline=True)	
    embed.add_field(name="s!matar", value="como usar ``ls!matar @usuário`` Use esse comando se alguem estiver merecendo!", inline=True)
    embed.add_field(name="ls!falar", value="como usar ``ls!falar <qualquercoisa>`` Faça eu falar alguma coisa!", inline=True)
    embed.add_field(name="s!suicidio", value="como usar ``ls!suicidio`` suicidio💔", inline=True)
    embed.add_field(name="ls!chorar", value="como usar ``ls!chorar`` Chorar faz bem para os olhos...", inline=True)
    embed.add_field(name="ls!votar", value="como usar ``ls!votar`` Faça uma votação em seu servidor", inline=True)
    embed.add_field(name="ls!pergunta", value="como usar ``ls!pergunta`` me faça uma pergunta!", inline=True)
    embed.add_field(name = 'ls!userinfo ',value ='Como usar ``ls!userinfi @usuário`` Veja as informações do usuário marcado!',inline = False)
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando diversaoajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))
			
					
	
	
@bot.command(pass_context=True)
async def userinfo(ctx):
		id = ctx.message.author.id
		if id in amounts:
			embed = discord.Embed(title="userinfo {}".format(ctx.message.author.name), description="Reflexão: Hoje n tem reflexão :(", color=0x00ff00)
			embed.add_field(name="Nome", value=ctx.message.author.name, inline=True)
			embed.add_field(name="ID do usuário", value=ctx.message.author.id, inline=True)
			embed.add_field(name="Status do usuário", value=ctx.message.author.status, inline=True)
			embed.add_field(name="Melhor cargo", value=ctx.message.author.top_role)
			embed.add_field(name="entrou no servidor", value=ctx.message.author.joined_at)
			embed.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
			await bot.say(embed=embed)
			print('comando perfil digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context = True)
async def modajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Comandos Moderação Help')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'ls!kick ',value ='como usar ``ls!kick @usuário`` Expulsa o usuário marcado',inline = False)
    embed.add_field(name = 'ls!ban ',value ='Como usar ``ls!ban @usuário`` bane o usuário marcado',inline = False)
    embed.add_field(name = 'ls!addrole ',value ='Como usar ``ls!addrole @role @usuário`` adiciona um determinado cargo ao usuário marcado',inline = False)
    embed.add_field(name = 'ls!removerole',value ='Como usar ``ls!removerole @role @usuário`` remove um determinado cargo do usuário marcado ',inline = False)
    embed.add_field(name = 'ls!clear',value ='Como usar ``s!clear`` apaga as mensagens do canal de texto atual ',inline = False)
    embed.add_field(name = 'ls!avisar',value ='Como usar ``s!avisar @usuário`` avisa um usuário no PV ',inline = False)
    embed.add_field(name = 'ls!setnick',value ='Como usar ``ls!setnick <nicknovo>`` De um novo apelido a um usuário ',inline = False)
    embed.add_field(name = 'ls!report',value ='Como usar ``ls!report @usuário <motivo>`` Reporte um usuário',inline = False)
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei mensagens em sua DM'.format(ctx.message.author.mention))
    print('comando modajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def serverinfo(ctx):
	embed = discord.Embed(name="{}' serverinfo".format(ctx.message.server.name), description="s!ajuda para ver meus comandos!.", color=0x00fA00)
	embed.add_field(name="📄Nome do servidor", value=ctx.message.server.name, inline=True)
	embed.add_field(name = '👑 Dono', value = str(ctx.message.server.owner) + '\n' + ctx.message.server.owner.id);
	embed.add_field(name="💻ID do servidor", value=ctx.message.server.id, inline=True)
	embed.add_field(name="🎓Total de roles", value=len(ctx.message.server.roles), inline=True)
	embed.add_field(name="👥Quantidade de Membros", value=len(ctx.message.server.members))
	embed.add_field(name='🌎 Região', value=ctx.message.server.region)
	embed.add_field(name='👮Role Top1', value=ctx.message.server.role_hierarchy[0])
	embed.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	embed.set_thumbnail(url=ctx.message.server.icon_url)
	await bot.say(embed=embed)
	print('comando serverinfo digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def avatar(ctx, user: discord.User):
	
	list = (user.avatar_url), (user.avatar_url)
	hug = random.choice(list)
	hugemb = discord.Embed(title='Avatar de {}'.format(user.name), color=0x6A1B9A)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando avatar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def roleta(ctx, *, pergunta: str = None):
    if not pergunta:
        return await bot.say("Você precisa perguntar alguma coisa.")
    else:
        resposta = choice(['Sim', 'Não', 'Talvez', 'Nunca', 'Claro'])
        embed = discord.Embed(color=0xFF0000)
        embed.add_field(name="Pergunta:", value='{}'.format(pergunta), inline=False)
        embed.add_field(name="Resposta:", value=resposta, inline=False)
        await bot.say(embed=embed)
        print('comando roleta digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voicemute(ctx, member: discord.Member):
    await bot.server_voice_state(member,mute=True)
    emb = discord.Embed(title='Usuário mutado voz', description='{} foi mutado com sucesso.'.format(member.mention), color=0xE57373)
    emb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
    await bot.say(embed=emb)  

@bot.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def voiceunmute(member: discord.Member):
	await bot.server_voice_state(member,mute=False)
	emb = discord.Embed(title='Usuário desmutado voz', description='{} foi desmutado com sucesso.'.format(member.mention), color=0x00ffbb)
	emb.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=emb)

@bot.command(pass_context = True)
async def ajuda(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'ls!modajuda ',value ='Comandos de moderação!',inline = False)
    embed.add_field(name = 'ls!diversaoajuda ',value ='Comandos de diversão e que todos podem usar!',inline = False)
    embed.set_footer(text='comando realizado por {}| Bot Oficial Legend•Squad'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei meus comandos la na sua DM'.format(ctx.message.author.mention))
    print('comando ajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
    
   
    
    embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
    embed.set_author(name='Ajuda')
    embed.set_image(url = 'https://image.ibb.co/caM2BK/help.gif')
    embed.add_field(name = 'ls!modajuda ',value ='Comandos de moderação!',inline = False)
    embed.add_field(name = 'ls!diversaoajuda ',value ='Comandos de diversão e que todos podem usar!',inline = False)
    embed.set_footer(text='comando realizado por {}| Bot Oficial Legend•Squad'.format(ctx.message.author.name))
    await bot.send_message(author,embed=embed)
    await bot.say('{} Enviei meus comandos la na sua DM'.format(ctx.message.author.mention))
    print('comando ajuda digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, limit: int=100):
    async for msg in bot.logs_from(ctx.message.channel, limit=limit):
            try:
                await bot.delete_message (msg)
            except:
                pass
    embed = discord.Embed(description="Chat limpo com sucesso! por {} :smile:".format(limit, ctx.message.author.mention), color=0x00ff00)
    embed.set_footer(text ='Comando pedido por: {} | Legend•Squad Oficial'.format(ctx.message.author.name))
    await bot.say (embed=embed)
    print('comando clear digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))

@bot.command(pass_context=True)
async def chorar(ctx):
	list = 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943338/tumblr_mchb17x02w1r5patso2_500.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648453943336/0319d0c4d6ce1750c2fc7b3c5d383723db18d37dr1-500-284_00.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913648034643972/86a31db739b7f40d576c90f1ff9329ab254958f0_hq.gif', 'https://cdn.discordapp.com/attachments/514045065929162764/540913647610757130/cfd934eac0f14d3f43284b16ec0a902b.gif'
	
	
	
	hug = random.choice(list)
	hugemb = discord.Embed(title='Chorar...',  description='😭| **{}** Esta chorando...'.format(ctx.message.author.name), color=0xA7ffbb)
	hugemb.set_image(url=hug)
	hugemb.set_footer(text ='Comando realizado por {} | Legend•Squad Oficial'.format(ctx.message.author.name))
	await bot.say(embed=hugemb)
	print('comando chorar digitado no servidor {} por {}'.format(ctx.message.server.name, ctx.message.author))



bot.run(str(os.environ.get('BOT_TOKEN')))
