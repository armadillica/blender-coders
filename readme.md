#blendercoders.xyz

This is a simple site with the only purpose of generating the timetable for the upcoming Blender developer meetings.

Run the development Docker image with:

```
docker run -ti -p 5555:5000 --name blendercoders -v /local/path/to/blender-coders:/data/git/blender-coders armadillica/blender_coders_dev
``

Run the production Docker image with:

```
docker run -ti -p 5555:80 --name blendercoders -v /local/path/to/blender-coders/blender-coders:/data/git/blender-coders armadillica/blender_coders_pro
```
