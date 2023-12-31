

from controller import Robot


class FireMovement(Robot):
    
    def __init__(self, fps=25):
       
        super(FireMovement, self).__init__()
        # self.timeStep = int(self.getBasicTimeStep())
        # set the control time step
        print('Initializing Fire Movement...', end=' ')
        self.timeStep = 1000 // fps  # 25fps => 40ms
        self.init_displays()
        self.load_sprites()
        print('OK')

    def init_displays(self):
       
        self.fire_screen = self.getDisplay("fireDisplay")
        self.smoke_screen = self.getDisplay("smokeDisplay")

    def load_sprites(self):
        self.fire_img = self.fire_screen.imageLoad(
            "320x320_fire_sprint.png")
        self.smoke_img = self.smoke_screen.imageLoad(
            "320x160_black_smoke_sprint.png")

        fire_coords = [0, -320, -640, -960]
        self.fire_frame_xy = [[x1, y1] for x1 in fire_coords
                              for y1 in fire_coords]
        self.n_fire_frames = len(self.fire_frame_xy)

        smoke_coords = [0, -160, -320]
        smoke_frame_xy = [[y1, x1] for x1 in fire_coords
                          for y1 in smoke_coords]
        self.smoke_frame_xy = smoke_frame_xy[6:11]
        self.n_smoke_frames = len(self.smoke_frame_xy)

    def move_fire(self, step=-1):
        frame = step % self.n_fire_frames
        pos = self.fire_frame_xy[frame]
        self.fire_screen.imagePaste(self.fire_img, pos[0], pos[1], False)

    def move_smoke(self, step=-1):
        # ts = step -5 if step > 11 else step
        # if step <= 11:
        # 	smoke_xy = smoke_frame_xy
        # 	n_frames = smoke_frames
        # else: # for increasing cloud
        # 	smoke_xy = smoke_repeat_xy
        # 	n_frames = smoke_repeat_frames
        frame = step % self.n_smoke_frames
        pos = self.smoke_frame_xy[frame]
        self.smoke_screen.imagePaste(self.smoke_img, pos[0], pos[1], False)

    def run(self):
        # main control loop:
        print('Running...')
        counter = 1
        while self.step(self.timeStep) != -1:
            self.move_smoke(counter)
            self.move_fire(counter)
            counter += 1

    def __del__(self):
        self.smoke_screen.imageDelete(self.smoke_img)
        self.fire_screen.imageDelete(self.fire_img)


if __name__ == '__main__':
    # run controller
    controller = FireMovement()
    controller.run()
