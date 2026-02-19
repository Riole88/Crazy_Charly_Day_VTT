INSERT INTO "article" ("id", "designation", "category", "age","state", "price", "weight") VALUES
                                                                                              ('9d4fb305-6eb7-48f3-9c70-da9cbfde6fd8', 'Monopoly Junior', 'SOC', 'PE', 'N', 8, 400),
                                                                                              ('c5c9fdc3-97b7-43ce-be4c-6bb9ca6d6f62', 'Barbie Aventurière', 'FIG', 'PE', 'TB', 5, 300),
                                                                                              ('28bb365c-db67-460a-93f2-19a9d16328fd', 'Puzzle éducatif', 'EVL','PE', 'TB', 7, 350 );

INSERT INTO "users" ("id", "email", "lastName", "firstName", "password", "preferences")
VALUES('9dc8ea98-83d3-44d3-b48a-b3d903758d25','pert.emma@mail.com','Pert','Emma','password1','SOC,FIG,EVL,CON,LIV,EXT');



INSERT INTO "box" ("id", "name", "totalPrice", "totalWeight", "score") VALUES ('f47ac10b-58cc-4372-a567-0e02b2c3d479', 'Ma Box de Jeux', 15.00, 750.00, 5);


INSERT INTO "users2box" ("id", "idUser", "idBox") VALUES ('0701a7b8-a6df-495c-9d17-678d2b4bc483', '9dc8ea98-83d3-44d3-b48a-b3d903758d25', 'f47ac10b-58cc-4372-a567-0e02b2c3d479');


INSERT INTO "article2box" ("id", "idArticle", "idBox") VALUES ('f7a0e1fb-f476-47cb-9d86-62443d64d468', '9d4fb305-6eb7-48f3-9c70-da9cbfde6fd8', 'f47ac10b-58cc-4372-a567-0e02b2c3d479'),
                                                              ('eb7daa4f-905e-4328-b472-eaf5b6f248b5', '28bb365c-db67-460a-93f2-19a9d16328fd', 'f47ac10b-58cc-4372-a567-0e02b2c3d479');
