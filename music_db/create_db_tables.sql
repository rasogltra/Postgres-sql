CREATE TABLE "users" (
  "user_id" integer PRIMARY KEY,
  "username" varchar,
  "email" varchar,
  "subscriber_plan" varchar,
  "region" varchar,
  "created_at" timestamp
);

CREATE TABLE "artists" (
  "artist_id" integer PRIMARY KEY,
  "name" varchar,
  "genre" varchar
);

CREATE TABLE "albums" (
  "album_id" integer PRIMARY KEY,
  "artist_id" integer,
  "title" varchar,
  "release_date" timestamp
);

CREATE TABLE "tracks" (
  "track_id" integer PRIMARY KEY,
  "album_id" integer,
  "title" varchar,
  "duration" timestamp
);

CREATE TABLE "listening_sessions" (
  "session_id" integer PRIMARY KEY,
  "user_id" integer,
  "track_id" integer,
  "region" varchar,
  "skip_count" integer,
  "device_type" varchar
);

CREATE TABLE "products" (
  "product_id" integer PRIMARY KEY,
  "artist_id" integer,
  "type" varchar,
  "price" float,
  "qty" integer
);

CREATE TABLE "orders" (
  "order_id" integer PRIMARY KEY,
  "user_id" integer,
  "order_date" timestamp,
  "total_amount" float,
  "status" varchar
);

CREATE TABLE "order_items" (
  "item_id" integer PRIMARY KEY,
  "order_id" integer,
  "product_id" integer,
  "qty" integer,
  "item_price" float
);

ALTER TABLE "albums" ADD FOREIGN KEY ("artist_id") REFERENCES "artists" ("artist_id");

ALTER TABLE "albums" ADD FOREIGN KEY ("album_id") REFERENCES "tracks" ("album_id");

ALTER TABLE "listening_sessions" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("user_id");

ALTER TABLE "tracks" ADD FOREIGN KEY ("track_id") REFERENCES "listening_sessions" ("track_id");

ALTER TABLE "users" ADD FOREIGN KEY ("user_id") REFERENCES "orders" ("user_id");

ALTER TABLE "artists" ADD FOREIGN KEY ("artist_id") REFERENCES "products" ("artist_id");

ALTER TABLE "order_items" ADD FOREIGN KEY ("product_id") REFERENCES "products" ("product_id");

ALTER TABLE "order_items" ADD FOREIGN KEY ("order_id") REFERENCES "orders" ("order_id");
