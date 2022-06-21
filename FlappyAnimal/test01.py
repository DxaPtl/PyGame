import pygame
import game as g
import gameSettings as gs
def ScoreBoard(IsGame, score):
	if IsGame == 'MainGame':
		ScoreBlock = g.SmallFont.render(str(int(gs.SCORE)),True, gs.WHITE)
		ScoreRect = ScoreBlock.get_rect(topleft = (20,20))
		g.screen.blit(ScoreBlock,ScoreRect)
	elif IsGame == 'GameOver':
         HSCORE = g.UserData['HIGHSCORE']
         if int(score) > HSCORE:
            g.UserData['HIGHSCORE'] = score
         return g.UserData['HIGHSCORE']

print("Highest Score: "+ScoreBoard("GameOver", 50))