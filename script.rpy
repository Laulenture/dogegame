# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define d = Character("Doge")
define g = Character("Gabe")
define i = Character("Illulinaty")
define e = Character("EA")
# The game starts here.

label start:
    scene location black
    d "frer?"
    d "FRer?"
    d "FRER!!"

    scene location bedroom
    show doge angry  
    d "Frer, on a plus de chocapic. C'est la galère!!!"
    d "Et le pire c'est qu'on n'a plus de cash!"
    show doge happy
    d "Mais t'inquiet j'ai la solucion des familles"
    d "On va miner comme jaja"
    d "Et on va miner un truc incroyable. On va rentrer dans les annales du minage."
    show doge mlg 
    d "On va miner des DOGECOIN!"
    d "Mais tkt on va pas aller a la mine, trop la flemme. On va se faire un pc et il le fera pour nous."
    d "Mais comment on va faire."
    menu: 
     " "
     "T'a une idée.":
      jump matrix
     "Flemme":
      jump flemme
     "LDLC":
      jump ldlc

#partie gauche
label ldlc:
    scene location ldlc
    show doge happy
    $ menu_flag = True

    d "On est arriver a ldlc."
    d "On fais quoi ?"
    menu:
     "Enfaite j'ai la flemme.":
      jump finflemme
     "On va voir pour un pc.":
      jump choixpc

label choixpc:
    scene location ldlc
    show  doge happy

    d "Je viens de regarder les prix c'est pas donné."
    d "On le paye comment ? Ou t'es chaud pour un vol ?"
    menu:
     "Voler le pc ":
      jump finvol
     "Chercher un moyen de le financer":
      jump finance

label finvol:
    scene location prison
    show doge triste
    d"C'était pas vraiment une bonne idée"
    scene location black
    "FIN"
    return

label finance:
    scene location ldlc
    show doge happy
    d "Ouais mais on trouve cette argent où mec ?"
    menu:
     "On vol cet argent bien sûr !":
      jump illegal
     "Y'a forcément un moyen de faire ça dans les règles.":
      jump legal
    
label illegal:
    scene location ldlc
    show doge happy
    d "Ok mais cette argent on le vol où ?"
    menu:
     "On vol la déclaration d'indépendance !":
      jump findeclaration
     "On cambriole une banque bien sûr !":
      jump cambriolage

label findeclaration:
    scene location prison
    show doge triste
    d "On a visé peut-être un peut haut non ?"
    scene location black
    "FIN"
    return

label cambriolage:
    scene location ldlc
    show doge happy
    d "Dans ce cas on cambriole quelle..."
    d "Viens on va discuter de ça dehors"
    scene location rue
    show doge happy
    d"On cambriole quelle banque ?"
    menu:
     "La réserve nationnal !":
      jump finreservenationnal
     "Une petite banque genre la Caisse D'épargne de Tournan-en-Brie.":
      jump tournanenbrie

label finreservenationnal:
    scene location rnus
    show doge mlg
    d"Ca va être du gâteau frer."
    scene location prison
    show doge triste
    d"On y était prèsque pourtant."
    return

label tournanenbrie:
    scene location rue
    show doge mlg
    d"Tu veux faire ça comment ?"
    menu:
     "On défonce tout":
      jump finfrontal
     "On y va discretement":
      jump findiscretement

label finfrontal:
    scene location banque
    show doge mlg
    d"On entre, on prend tous et on se casse !"
    scene location prison
    show doge angry
    d"Je pouvais pas savoir que un convois policier passait à ce moment !"
    return

label findiscretement:
    scene location banque
    show doge mlg
    d"On y va discrètement, aucun bruit, tel un ninja."
    scene location prison
    show doge triste
    d"Tu savais que les portes du coffre fort se ferment automatiquement ? Moi non plus"
    return

label legal:
    scene location ldlc
    show doge happy
    d"Et tu veux gagner cet argent comment ?"
    menu:
     "Grand mère à la retraite non ?":
      jump grandmere
     "Je sais !! On va monter une start-up ! Une boite qui va miner pour nous.":
      jump monterstartup
     "Y'a forcément moyen de se faire du fric avec les cours de la bourse !":
      jump finbourse

label finbourse:
    scene location bedroom
    show doge triste
    d"Pourquoi ça dis que notre balance est à -1463 euros ?"
    return



#parti central 
label flemme:

        $ menu_flag = False

        d "Faut trouver un job alors."
        menu:
            "Ouais mais flemme.":
                 jump finflemme

            "Direction pôle emploi.":
                  jump travail

label finflemme:
    show doge triste
    d "Ok pas de chocapic on attend le mois prochain avec la bourse sniff..."
    return
label travail:
    scene location pole_emploi
    show doge happy
    d "On a deux jobs a nôtre portée."
    menu:
     "Starbucks":
      jump finstarbucks

     "McDonald's":
       jump finmcdo

label finstarbucks:
    scene location starbucks
    show doge happy
    d "Au moins on paye pas le café."
    scene panel starbucks
    "FIN Starbucks."
    return

label finmcdo:
    scene location mcdonalds
    show doge happy
    d "Au moins on a des Big Burgers."
    scene panel mcdo
    "FIN McDonald's."
    return


     

