const gulp = require("gulp");
const replace = require("gulp-replace");
const concat = require("gulp-concat");
const css2js = require("gulp-css2js");
const htmlreplace = require("gulp-html-replace");

gulp.task("unite-css", () => {
  return gulp
    .src("./build/static/css/*.css")
    .pipe(concat("styles.css"))
    .pipe(css2js({ splitOnNewline: false }))
    .pipe(gulp.dest("./build/static/js"));
});

gulp.task("bundle", () => {
  return gulp
    .src("./build/static/js/*.js")
    .pipe(concat("main.js"))
    .pipe(replace("ReactDom", "ReactDOM"))
    .pipe(gulp.dest("./dist"));
});

gulp.task("copy-public", () => {
  return gulp
    .src(["./public/**", "!./public/index.html"])
    .pipe(gulp.dest("./dist"));
});

gulp.task("copy-media", () => {
  return gulp
    .src("./build/static/media/**")
    .pipe(gulp.dest("./dist/static/media"));
});

gulp.task("replace", () => {
  return gulp
    .src("./public/index.html")
    .pipe(htmlreplace({ js: "main.js" }))
    .pipe(gulp.dest("./dist"));
});

gulp.task(
  "default",
  gulp.series("unite-css", "bundle", "copy-public", "copy-media", "replace")
);
