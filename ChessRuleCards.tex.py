#!/usr/bin/env python3

import os
import re

import itertools

def TikZ_sidebar_card(card):
    CARD_TEMPLATE = [
    r'''\begin{tikzpicture}
    \pgfmathsetmacro{\cardroundingradius}{4mm}
    \pgfmathsetmacro{\striproundingradius}{3mm}
    \pgfmathsetmacro{\cardwidth}{5.9}
    \pgfmathsetmacro{\cardheight}{9.2}
    \pgfmathsetmacro{\stripwidth}{1.2}
    \pgfmathsetmacro{\strippadding}{0.1}
    \pgfmathsetmacro{\textpadding}{0.3}
    \pgfmathsetmacro{\ruleheight}{0.1}
    \providecommand{\stripfontsize}{\Huge}
    \providecommand{\captionfontsize}{\LARGE}
    \providecommand{\textfontsize}{\large}
    \draw[rounded corners=\cardroundingradius] (0,0) rectangle (\cardwidth,\cardheight);
    \fill[''',
    r''',rounded corners=\striproundingradius] (\strippadding,\strippadding) rectangle (\strippadding+\stripwidth,\cardheight-\strippadding) node[rotate=90,above left,black,font=\stripfontsize] {''',
    r'''};
    \node[text width=(\cardwidth-\strippadding-\stripwidth-2*\textpadding)*1cm,below right,inner sep=0] at (\strippadding+\stripwidth+\textpadding,\cardheight-\textpadding) 
    {   {\captionfontsize ''',
    r'''}\\ 
        {\textfontsize ''',
    # r'''}\\
        # \tikz{\fill (0,0) rectangle (\cardwidth-\strippadding-\stripwidth-2*\textpadding,\ruleheight);}\\
        # {\captionfontsize ''',
    r'''}\\
        \tikz{\fill (0,0) rectangle (\cardwidth-\strippadding-\stripwidth-2*\textpadding,\ruleheight);}\\
        {\textfontsize ''',
    r'''}\\
    };
    \end{tikzpicture}%''',
    ]

    striptext = card['striptext'] + r' \rotatebox[origin=c]{-90}{' + card['stripsymbol'] + r'}'
    CARD_DATA = [card['stripcolor'], striptext, card['topcaption'], card['topcontent'], card['bottomcontent']]
    # CARD_DATA = [card['stripcolor'], striptext, card['topcaption'], card['topcontent'], card['bottomcaption'], card['bottomcontent']]
    CARD_TEX = itertools.chain(*itertools.zip_longest(CARD_TEMPLATE, CARD_DATA, fillvalue=''))
    # for v in CARD_TEX:
        # print(v)
    # print((CARD_TEX))
    print(''.join(CARD_TEX))

def TikZ_card(card):
    CARD_TEMPLATE = [
    r'''\begin{tikzpicture}
    \pgfmathsetmacro{\cardroundingradius}{4mm}
    \pgfmathsetmacro{\striproundingradius}{3mm}
    \pgfmathsetmacro{\cardwidth}{5.9}
    \pgfmathsetmacro{\cardheight}{9.2}
    \pgfmathsetmacro{\stripwidth}{1.2}
    \pgfmathsetmacro{\strippadding}{0.1}
    \pgfmathsetmacro{\textpadding}{0.3}
    \pgfmathsetmacro{\ruleheight}{0.1}
    \providecommand{\stripfontsize}{\Huge}
    \providecommand{\captionfontsize}{\LARGE}
    \providecommand{\textfontsize}{\Large}
    \providecommand{\quotefontsize}{\small}
    \draw[line width=2mm,rounded corners=\cardroundingradius] (0,0) rectangle (\cardwidth,\cardheight);
    \node[text width=(\cardwidth-\strippadding-2*\textpadding)*1cm,below right,inner sep=0] at (\strippadding+\textpadding,\cardheight-\textpadding) 
    { 
    \begin{center} {\fontsize{90pt}{90pt}\selectfont ''',
    r'''}\\\end{center}
    \begin{center}
    {\captionfontsize \textsf{\textbf{''',
    r'''}}}\\ 
        \end{center}
        {\textfontsize ''',
    r'''}\\
        \tikz{\fill (0,0) rectangle (\cardwidth-2*\strippadding-2*\textpadding,\ruleheight);}\\
        {\quotefontsize \textit{''',
    r'''}}\\
    };
    \end{tikzpicture}%''',
    ]

    CARD_DATA = [card['stripsymbol'],card['topcaption'], card['topcontent'], card['bottomcontent']]
    # CARD_DATA = [card['stripcolor'], striptext, card['topcaption'], card['topcontent'], card['bottomcaption'], card['bottomcontent']]
    CARD_TEX = itertools.chain(*itertools.zip_longest(CARD_TEMPLATE, CARD_DATA, fillvalue=''))
    # for v in CARD_TEX:
        # print(v)
    # print((CARD_TEX))
    print(''.join(CARD_TEX))

def buildTeX(cards):
    TEX_HEADER = r'''
    % latexmk -pdflatex='lualatex' -pdf FontExhibition.tex
    \documentclass[parskip]{scrartcl}
    \usepackage{fontspec}
    \usepackage[margin=5mm]{geometry}
    \usepackage{tikz}
    \usepackage{pifont}
    \usepackage{graphicx}
    \usepackage{diagram}
    \usepackage{setspace}

    \begin{document}
    \setmainfont[Extension={.ttf},ItalicFont={DejaVuSerif-Italic}]{FreeSerif}
    '''

    TEX_FOOTER = r'''

    \begin{diagram}[5x5]
    \pieces{wLc3, wCa1, wCe1, wCa5, wCe5, wCa3, wCe3, wCc1, wCc5, wCc2, wCc4, wCb3, wCd3}
    \end{diagram}
    \begin{diagram}
    \source{Problemkiste} \year{1992}
    \dedic{Elmar Bartel gew.}
    \pieces[2+3]{wKd1, wBe2, sKh8, sBe4, sTa4}
    \stip{h\#7}
    \sol{1.Ta3 Kc2!, 2.Tf3 e\x f3, 3.e3 f4, 4.e2 f5, 5.e1T f6,
         6.Th1! (Te7?) f7, 7.Th7 f8D\#}
         \end{diagram}
         {
    {\fontsize{30pt}{30pt}\selectfont ♔♕♖♗♘♙♚♛♜♝♟♞}
    }
    \end{document}
    '''
    print(TEX_HEADER)
    for i, card in enumerate(cards):
        # TikZ_sidebar_card(card)
        TikZ_card(card)
        if i%3==2:
            print(r'\\[-\lineskip]')
    print(TEX_FOOTER)

cards = [
    {
     'stripsymbol':'♘',
     'topcaption':'LEND ME YOUR HORSE',
     'topcontent':'Non-pawn pieces protected by a knight may also move/take like a knight.',
     'bottomcontent':'''"You should know better than to mount another's war-horse", I said with a smirk. ---Jessica Leake''',
     },
    {
     'stripsymbol':'♘',
     'topcaption':'JEDI KNIGHT',
     'topcontent':'If you only have one knight on the board, it can also move and take like a Queen.',
     'bottomcontent':'''In my experience, when you think you understand the Force, you realize just how little you know. ---Ahsoka Tano''',
     },
    {
     'stripsymbol':'♙+',
     'topcaption':'PRECOCIOUS PAWNS',
     'topcontent':'Pawns start on the third rank. Draw another card.',
     'bottomcontent':'''Precocious was not the same as smart, much less the same as wise, and the perfect opposite of informed. ---Lionel Shriver''',
     },
    {
     'stripsymbol':'♙',
     'topcaption':'CHECKERS',
     'topcontent':'Pawns move and take like checkers.',
     'bottomcontent':'''These guys are playing checkers. I'm out here playing chess. When they figure it out, it's too late. ---Max Holloway''',
     },
    {
     'stripsymbol':'♙',
     'topcaption':'BEROLINA PAWNS',
     'topcontent':'Pawns move diagonally and take forward.',
        'bottomcontent':r'''Berolina is the female personification of Berlin and the allegorical female figure symbolizing the city. ---Wikipedia''',
     },
    {
     'stripsymbol':'♙+',
     'topcaption':'SHOGI PAWNS',
     'topcontent':'Pawns move and take one square forward. Two Shogi Pawns may not be placed in the same file. Draw another card.',
     'bottomcontent':'''If there is mate with a Pawn drop, there is a legal mate too. ---Shogi proverb''',
     },
    {
     'stripsymbol':'♙+',
     'topcaption':'FAST PAWNS',
     'topcontent':'Pawns capture normally, but may move any number of squares forward. Draw another card.',
     'bottomcontent':''' In ceremonies of the horsemen, even the pawn must hold a grudge. ---Bob Dylan''',
     },
    {
     'stripsymbol':'♙+',
     'topcaption':'BRIBE',
     'topcontent':'On your turn you can do an action by an enemy pawn instead. Draw another card.',
     'bottomcontent':'''Never underestimate the effectiveness of a straight cash bribe. ---Claud Cockburn''',
     },
    {
     'stripsymbol':'♙',
     'topcaption':'CHINESE CHECKERS',
     'topcontent':'Pawns take normally, but move like Chinese checkers (king move + hopping over other pawns).',
     'bottomcontent':r'''\tiny The Pentagon banned the army from using Chinese-made berets. In a more veiled slap at the Chinese, the Pentagon also banned any alternative form of checkers. ---Jimmy Fallon''',
     },
    {
     'stripsymbol':'♙+',
     'topcaption':'SIDE PAWNS',
     'topcontent':'Pawns may also capture sideways. Draw another card.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'♘',
     'topcaption':'NIGHT WIZARD',
     'topcontent':'Move/take life a giraffe [1,3], or one square diagonally [1,1]. Omega Chess Wizard.',
     'bottomcontent':'''Do not meddle in the affairs of Wizards, for they are subtle and quick to anger. ---J. R. R. Tolkien''',
     },
    {
     'stripsymbol':'♘',
     'topcaption':'TALLADEGA KNIGHTS',
     'topcontent':'Knights on your color may move/take like Rooks. Knights on your opponents colore may move/take like Bishops.',
     'bottomcontent':'''If you ain't first, you're last. ---Ricky Bobby''',
     },
    {
     'stripsymbol':'♔+',
     'topcaption':'TOUCHDOWN',
     'topcontent':'If your king is on the last rank at the end of your turn, you win. Draw another card.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'♔+',
     'topcaption':'SUMO KING',
     'topcontent':'Kings may take normally or shove billiards style. Pieces that fall of the edge die. Draw another card.',
     'bottomcontent':'''Good spirit! But you should push an opponent with more force! ---E. Honda''',
     },
    {
     'stripsymbol':'♔',
     'topcaption':'FAR MIMIC',
     'topcontent':'Kings act only as any friendly piece which can move to it. No castling. If pawn can move to king and king is on rank 2, can move 2 as pawn and be taken en-passant.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'♔',
     'topcaption':'NEAR MIMIC',
     'topcontent':'Kings act only as any adjacent friendly piece. No castling. If pawn can move to king and king is on rank 2, can move 2 as pawn and be taken en-passant.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'♔+',
     'topcaption':'KING OF THE HILL',
     'topcontent':'If your King makes a legal move into the center four squares, you win Mark. Draw another card.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'ANYTHING CAPTURES EN PASSANT',
     'topcontent':'Pieces may capture a piece that just moved through an area they attack.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'CAMOUFLAGE',
     'topcontent':'You can move through pieces on squares matching your color.',
     'bottomcontent':'''Camouflage is a game we all like to play, but our secrets are as surely revealed by what we want to seem to be as by what we want to conceal. ---Russell Lynes''',
     },
    {
     'stripsymbol':'\ding{72}+',
     'topcaption':'PARACHUTE',
     'topcontent':'You may pick up friendly pieces. Draw another card.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}+',
     'topcaption':'SACRIFICE',
     'topcontent':'You may take your own pieces. Draw another card.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'NEAR SWAP',
     'topcontent':'Two adjacent friendly pieces may swap places.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'KNIGHT SWAP',
     'topcontent':'Two friendly pieces which are a standard knight move apart may swap places.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'MOVE SWAP',
     'topcontent':'Two friendly pieces may swap places if one can move to or take the other.',
     'bottomcontent':'''Quote needed''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'UNFAIR',
     'topcontent':'Deal a card. It only applies to white or black; white decides. Repeat for black decides.',
     'bottomcontent':'''I know the world isn't fair, but why isn't it ever unfair in my favor? ---Bill Watterson''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'UNFAIR',
     'topcontent':'Deal a card. It only applies to white or black; white decides. Repeat for black decides.',
     'bottomcontent':'''I know the world isn't fair, but why isn't it ever unfair in my favor? ---Bill Watterson''',
     },
    {
     'stripsymbol':'\ding{114}',
     'topcaption':'BOUNCE',
     'topcontent':'The board continues by reflection in the outer ranks and files.',
     'bottomcontent':'''Success is how high you bounce when you hit bottom. ---George S. Patton''',
     },
    {
     'stripsymbol':'\ding{114}',
     'topcaption':'CYLINDER',
     'topcontent':'Pieces may move as if the right and left side of the board are adjacent to each other.',
     'bottomcontent':'''Everything in nature takes its form from the sphere, the cone and the cylinder. ---Paul Cezanne''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'PROFESSIONAL COURTESY',
     'topcontent':'Pieces do not attack or capture a piece of the same type. Pawns are not professional.',
     'bottomcontent':'''Courtesy is contagious - let's start an epidemic. ---Evan Esar''',
     },
    {
     'stripsymbol':'\ding{114}',
     'topcaption':'INSANE CYLINDER',
     'topcontent':'Pieces do not move/take backwards. The top and bottom of the board are considered adjacent.',
     'bottomcontent':'''There's a fine line between genius and insanity. I have erased this line. ---Oscar Levant''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'MOVE THROUGH FRIENDLY PIECES',
     'topcontent':'Friendly pieces do not block movement.',
     'bottomcontent':'''True friends stab you in the front. ---Oscar Wilde''',
     },
    {
     'stripsymbol':'++',
     'topcaption':'COMPLICATE',
     'topcontent':'Deal two more cards.',
     'bottomcontent':'''When all else fails, complicate matters. ---Aaron Allston''',
     },
    {
     'stripsymbol':'++',
     'topcaption':'COMPLICATE',
     'topcontent':'Deal two more cards.',
     'bottomcontent':'''Progress is man's ability to complicate simplicity. ---Thor Heyerdahl''',
     },
    {
     'stripsymbol':'+++',
     'topcaption':'CHAOS',
     'topcontent':'Deal three more cards.',
     'bottomcontent':'''Life is nothing without a little chaos to make it interesting. ---Amelia Atwater-Rhodes''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'SUPREME SACRIFICE',
     'topcontent':'You may remove any number of friendly pieces before your turn.',
     'bottomcontent':'''The speed of your success is limited only by your dedication and what you're willing to sacrifice. ---Nathan W. Morris''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'MOVE TWICE',
     'topcontent':'Move twice, or any other action once.',
     'bottomcontent':'''When someone says you can't do something, do it twice and take pictures. ---Anonymous''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'TAKE TWICE',
     'topcontent':'Take twice, or any other action once.',
     'bottomcontent':'''As long as I breathe, I attack. ---Bernaud Hinault''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'EXTINCTION',
     'topcontent':'You lose if you lose all of any piece.',
        'bottomcontent':'''Extinction is the rule. Survival is the exception. ---Carl Sagan''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'CROWDSURFING',
     'topcontent':'Any non-King piece can crowdsurf.',
     'bottomcontent':'''The joy of surfing is so many things combined, from the physical exertion of it to the challenge of it, to the mental side of the sport. ---Kelly Slater''',
     },
    {
     'stripsymbol':'\ding{72}',
     'topcaption':'OOBLEK',
     'topcontent':'Pieces must move as far as legally possible.',
     'bottomcontent':'''To me, if life boils down to one thing, it's movement. To live is to keep moving. ---Jerry Seinfeld''',
     },
    {
     'stripsymbol':'\ding{114}+',
     'topcaption':'10x10 BOARD',
     'topcontent':'The legal playing area now surrounds the board. Draw another card.',
     'bottomcontent':'''I don't have anything against walls. You know what it is? I like open spaces. ---Dion Dublin''',
     },
    {
     'stripsymbol':'?',
     'topcaption':'TELEPORTER',
     'topcontent':'Identify the piece type adjacent to the King towards the center as a teleporter. Teleporters may move to any square adjacent to a pawn.',
     'bottomcontent':'''If I could teleport, I'd probably still be late. --Anonymous''',
     },
    {
     'stripsymbol':'♘♗',
     'topcaption':'MINOR TENET',
     'topcontent':'Bishops move and take backwards like Knights. Knights move and take backward like Bishops.',
     'bottomcontent':'''Bold I'm Fine With. I Thought You Were Gonna Say Nuts. ---Mahir''',
     },
    {
     'stripsymbol':'♘♗',
     'topcaption':'BISHOP-KNIGHT SWAP',
     'topcontent':'Bishops take like Knights. Knights take backward like Bishops. Both move normally.',
     'bottomcontent':'''Quote needed''',
     },
    { 'stripsymbol':'♕',
     'topcaption':'NIGHT KING QUEEN',
     'topcontent':'Queens move and take like Knight+King.',
     'bottomcontent': r'''Night's King was only a man by light of day, Old Nan would always say, but the night was his to rule. ---Brandon Stark''',
     },
    { 'stripsymbol':'♕',
     'topcaption':'BISHOP-KNIGHT QUEEN',
     'topcontent':'Queens move and take like Bishop+Knight. Fairy chess Archbishop.',
     'bottomcontent': r'''If people want a sense of purpose they should get it from their archbishop. They should certainly not get it from their politicians. ---Harold MacMillan''',
     },
    { 'stripsymbol':'♕',
     'topcaption':'ROOK-KNIGHT QUEEN',
     'topcontent':'Queens move and take like Rook+Knight. Fairy chess Chancellor.',
     'bottomcontent': r'''When I'm stirring a saucepan, I don't say to myself, 'Now the chancellor is stirring a saucepan'. ---Angela Merkel''',
     },
    { 'stripsymbol':'♗',
     'topcaption':'CROWNED BISHOP',
     'topcontent':'Bishops may also move/take live a King.',
     'bottomcontent': r'''Quote needed''',
     },
    { 'stripsymbol':'♖',
     'topcaption':'CROWNED CASTLE',
     'topcontent':'Rooks may also move/take live a King.',
     'bottomcontent': r'''Quote needed''',
     },
    { 'stripsymbol':'♖',
     'topcaption':'CHINESE CANNON',
     'topcontent':'A rook takes by throwing a friendly piece so that it jumps the rook in a rook direction.',
     'bottomcontent': r'''Quote needed''',
     },
    { 'stripsymbol':'♖',
     'topcaption':'SIEGE TOWER',
     'topcontent':'A piece may move legally to where there is a rook. It goes on top making a combined piece. The combination acts as the bottom rook. The piece on top can move off as a normal action. Stacks are ok. Multi-color is ok.',
     'bottomcontent': r'''Quote needed''',
     },
    { 'stripsymbol':'♖',
     'topcaption':'IMMOBILIZER',
     'topcontent':'Pieces adjacent to an enemy Rook may not move. Rooks may not capture. Ultima Chess.',
     'bottomcontent': r'''The activity of worrying keeps you immobilized. ---Wayne Dyer''',
     },
    { 'stripsymbol':'♖♗',
     'topcaption':'ROYAL REVERSE',
     'topcontent':'Bishops and Rooks may move and take backwards like a Queen.',
     'bottomcontent': r'''To the royal guards of this realm, we are all victims in-waiting. ---Cheshire Cat''',
     },
    { 'stripsymbol':'♖♕',
     'topcaption':'ROOK-QUEEN SWAP',
     'topcontent':'Queens and Rooks move normally, but take like each other.',
     'bottomcontent': r'''I am definitely the queen. I definitely see myself as the queen. ---Lil' Kim''',
     },
    { 'stripsymbol':'♘♔',
     'topcaption':'KNIGHT-KING SWAP',
     'topcontent':'Knights and Kings move/take like each other.',
     'bottomcontent': r'''Quote needed''',
     },
    { 'stripsymbol':'♔',
     'topcaption':'KING CHAMELEON',
     'topcontent':'Kings may also move/take like any piece attacking them.',
     'bottomcontent': r'''I can kind of be a chameleon. ---Sasha Spielberg''',
     },
    {'striptext':'SUMMONER',
     'stripsymbol':'♗',
     'stripcolor':'cyan',
     'topcaption':'SUMMONER',
     'topcontent':'Bishops may summon a friendly non-King piece to an adjacent square',
     'bottomcaption':'Q m,x N+K',
     'bottomcontent': r'''My name is Mortimer Alexander and I am a licensed summoner." "Darn. I'd hoped you were the pizza delivery guy. ---Jana Oliver'''
     },
    {'stripsymbol':'♗',
     'topcaption':'BISHOP CHAMPION',
     'topcontent':'Bishops may move/take using a 2 square jump in any direction. They may also move/take one square rectilinearly.',
     'bottomcaption':'B m,x [2,2],[1,0],[2,0]',
     'bottomcontent': r'''Omega Chess Champion'''
     },
    {'stripsymbol':'♗',
     'topcaption':'RETREATER',
     'topcontent':'Bishops move like a queen, but take by moving away from an adjacent piece.',
     'bottomcontent': r'''He who fights and runs away, lives to fight another day. ---Proverb'''
     },
    {'stripsymbol':'♗',
     'topcaption':'BANISHER',
     'topcontent':'Bishops can banish any adjacent enemy piece to any empty square. Bishops move like Queens, but cannot capture.',
     'bottomcontent': r'''I know that you cannot banish the truth permanently, you can only cloud it temporarily. ---Javed Jaffrey'''
     },
    {'stripsymbol':'♗',
     'topcaption':'BISHOP CHAMELEON',
     'topcontent':'Bishops move normally, but only attack pieces that attack them. Bishops attack each other normally. Ultima Chess.',
     'bottomcontent': r'''Quote needed'''
     },
    {'stripsymbol':'♗',
     'topcaption':'BISHOP LONG LEAPER',
     'topcontent':'Bishops move like a queen, but take by leaping over a piece. Ultima Chess.',
     'bottomcontent': r'''That's one small step for a man, one giant leap for mankind. ---Neil Armstrong'''
     },
    {'stripsymbol':'♗',
     'topcaption':'CLERICAL CLONES',
     'topcontent':'Bishops may move/take like the last piece the opponent moved.',
     'bottomcontent': r'''I'm starting to see players copy what I do. I'm flattered. ---Dennis Rodman'''
     },
    ]
        # body.append('\nTHE QUICK BROWN FOX jumped over the lazy dog.♔♕♖♗
     # ♙♚♛♜♝♞♟\n')
    # % \newcommand\chesspieces{♔♕♖♗♘♙♚♛♜♝♟♞}

if __name__ == '__main__':
    buildTeX(cards)

