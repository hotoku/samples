import { Field, ObjectType } from "type-graphql";

@ObjectType()
export class Team {
  @Field()
  id!: number;
  @Field()
  name!: string;
}
