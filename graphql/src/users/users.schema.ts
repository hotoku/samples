import { Field, ObjectType, InputType } from "type-graphql";
import { Team } from "../teams/teams.schema";

@ObjectType()
export class User {
  @Field()
  id!: number;
  @Field()
  name!: string;
  @Field()
  email!: string;
  @Field()
  team!: Team;
}

@InputType()
export class UserInput implements Pick<User, "name" | "email"> {
  @Field()
  name!: string;
  @Field()
  email!: string;
}
