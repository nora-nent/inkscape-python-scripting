import inkex

class setColor(inkex.ColorExtension):
    def modify_color(self, name, color):
        if (name == "fill"):
            return inkex.Color((255,0,0))
        elif (name == "stroke"):
            return inkex.Color((0,0,255))

if __name__ == '__main__':
    setColor().run()
