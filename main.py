def on_on_overlap(sprite, otherSprite):
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    game.set_dialog_cursor(img("""
        ........................
                ........................
                ........................
                ........................
                ..........ffff..........
                ........ff1111ff........
                .......fb111111bf.......
                .......f11111111f.......
                ......fd11111111df......
                ......fd11111111df......
                ......fddd1111dddf......
                ......fbdbfddfbdbf......
                ......fcdcf11fcdcf......
                .......fb111111bf.......
                ......fffcdb1bdffff.....
                ....fc111cbfbfc111cf....
                ....f1b1b1ffff1b1b1f....
                ....fbfbffffffbfbfbf....
                .........ffffff.........
                ...........fff..........
                ........................
                ........................
                ........................
                ........................
    """))
    game.show_long_text("try to say something else", DialogLayout.BOTTOM)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
mySprite = sprites.create(img("""
        ........................
            ..........bbbb..........
            ........bbddddbb........
            .......bddbbbbddb.......
            ......bdbbddddbbdb......
            .....bdbbdbbbbdbbdb.....
            .....bdbdbddddbdbdb.....
            .....cdbbdbbbbdbbdc.....
            .....cbdbbddddbbdbc.....
            .....efbddbbbbddbce.....
            .....eeffbddddbccee.....
            .....eeeeffcccceee......
            .....ceeeeeeeeeeee......
            .....ceeeeeeeeeeee......
            .....feeeeeeeeeeee......
            .....cceeeeeeeeeee......
            ......feeeeeeeeeee......
            .....6fceeeeeeeeee6.....
            ....6776eeeeeeeee676....
            ...6777666eeee6666776...
            ..67768e67766777667776..
            ...668ee7768867788666...
            ......ee77eeee77ecee....
            ......ee6eeeeee6eef.....
    """),
    SpriteKind.player)
info.set_life(5)
controller.move_sprite(mySprite, 100, 100)
mySprite.set_stay_in_screen(True)
scene.camera_follow_sprite(mySprite)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
mySprite2 = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            ..........ffff..........
            ........ff1111ff........
            .......fb111111bf.......
            .......f11111111f.......
            ......fd11111111df......
            ......fd11111111df......
            ......fddd1111dddf......
            ......fbdbfddfbdbf......
            ......fcdcf11fcdcf......
            .......fb111111bf.......
            ......fffcdb1bdffff.....
            ....fc111cbfbfc111cf....
            ....f1b1b1ffff1b1b1f....
            ....fbfbffffffbfbfbf....
            .........ffffff.........
            ...........fff..........
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
mySprite2.set_position(141, 38)
game.splash("Hashbrowns", "stop Larry the Litterer")
tiles.place_on_random_tile(mySprite, sprites.castle.tile_grass3)
pause(2000)

def on_forever():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            ..............bbbbbbb...........
                    ...........bb66663333baa........
                    .........bb3367776333663aa......
                    ........b33333888333389633aa....
                    .......b3333333333333389633aa...
                    ......b34443333333333338633bae..
                    .....b3455433333333334443333ae..
                    ....b33322333dddd3333455233daee.
                    ...b3d333333dd3bbbb33322333dabe.
                    ..b3d333333d3bb33bb33333333da4e.
                    ..bd33333333b33aab3333333223a4ee
                    .b3d3663333b33aab33366332442b4ee
                    .bd3b983333a3aa3333387633ee3b4ee
                    .bd6983333baaa333333387633bb4bee
                    b3d6833333bba333333333863ba44ebe
                    bdd3333333bb3333333333333a44bebe
                    add666633333322333366333ba44bbbe
                    ad67776333332442336983d3a444b4e.
                    add888b333333ee3369833d3a44b44e.
                    add333333333333336833d3a444b4e..
                    a3dd3333344433333dddd3a444b44e..
                    ab33ddd325543333dd33aa444b44e...
                    .eabb3dd32233333baaa4444b44e....
                    .ebabb3d333d33baa444443b44e.....
                    ..ebaab3ddd3aaa4444433b44e......
                    ..eebbaab33a44444333b444e.......
                    ...eeebbaab444b333b4444e........
                    ....ebeeebbbbbbbb4444ee.........
                    .....eebbbb44444444ee...........
                    .......eeebbb444eee.............
                    ..........eeeeee................
                    ................................
        """),
        mySprite2,
        randint(40, 50),
        randint(40, 50))
    pause(2000)
forever(on_forever)
