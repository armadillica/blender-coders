var gulp          = require('gulp'),
    plumber       = require('gulp-plumber'),
    sass          = require('gulp-sass'),
    sourcemaps    = require('gulp-sourcemaps'),
    autoprefixer  = require('gulp-autoprefixer'),
    jade          = require('gulp-jade'),
    uglify        = require('gulp-uglify'),
    concat        = require('gulp-concat'),
    livereload    = require('gulp-livereload'),
    inlinecss     = require('gulp-inline-css');

/* CSS */
gulp.task('styles', function() {
    gulp.src('blender-coders/src/styles/**/*.sass')
        .pipe(plumber())
        .pipe(sourcemaps.init())
        .pipe(sass({
            outputStyle: 'compressed'}
            ))
        .pipe(autoprefixer("last 3 version", "safari 5", "ie 8", "ie 9"))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('blender-coders/static/assets/css'))
        .pipe(livereload());
});

/* Inline CSS */
gulp.task('inlinecss', function() {
    return gulp.src('blender-coders/templates/widgets/*.html')
        .pipe(inlinecss({
            applyStyleTags: true,
            applyLinkTags: true,
            removeStyleTags: true,
            removeLinkTags: true
        }))
        .pipe(gulp.dest('blender-coders/templates/widgets'));
});

/* Templates - Jade */
gulp.task('templates', function() {
    gulp.src('blender-coders/src/templates/**/*.jade')
        .pipe(jade({
            pretty: false
        }))
        .pipe(gulp.dest('blender-coders/templates'))
        .pipe(livereload());
});

gulp.task('watch',function() {
    livereload.listen();

    gulp.watch('blender-coders/src/styles/**/*.sass',['styles']);
    gulp.watch('blender-coders/src/templates/**/*.jade',['templates']);
    // gulp.watch('blender-coders/templates/widgets/*.html',['inlinecss']);
});

gulp.task('default', ['styles', 'templates']);
