#blendercoders.xyz

This is a simple site with the only purpose of generating the timetable for the upcoming Blender developer meetings.

Run the production Docker image with:

```
docker run -ti -p 5555:80 --name blendercoders -v /Users/fsiddi/Developer/blender-coders:/data/git/blender-coders armadillica/blender_coders_pro
```