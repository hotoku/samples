import { Field, ObjectType, InputType } from "type-graphql";

@ObjectType()
export class Team {
  @Field()
  id!: number;
  @Field()
  name!: string;
}

@InputType()
export class TeamInput implements Pick<Team, "name"> {
  @Field()
  name!: string;
}
