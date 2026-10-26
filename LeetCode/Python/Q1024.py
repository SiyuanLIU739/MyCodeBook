class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        clips.sort(key = lambda x: (x[0], -x[1]))

        f = [1000] * (time + 1)
        f[0] = 0

        for clip in clips:
            for i in range(clip[0], min(clip[1] + 1, time + 1)):
                for j in range(clip[0], i):
                    f[i] = min(f[i], f[j] + 1)

        if(f[time] == 1000):
            return -1
        return f[time]