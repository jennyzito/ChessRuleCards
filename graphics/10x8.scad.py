import solid as sd

def board(x,y,square=10,rim=.1):
    box = sd.square([x*square,y*square])
    box -= sd.translate([rim,rim])(sd.square([8*square-rim*square,10*square-rim*square]))
    black = sd.square(square)
    for i in range((x+1)//2):
        for j in range(y):
            box += sd.translate([(2*i+(j&1))*square, j*square])(black)
    return box

if __name__ == '__main__':
    print(sd.scad_render(board(8,10)))
