import "reflect-metadata";
import { Query, Resolver, Mutation, Arg } from "type-graphql";
import { teams } from "../teams/teams.resolvers";
import { Team } from "../teams/teams.schema";
import { UserInput, User } from "./users.schema";

@Resolver(() => User)
export class UsersResolver {
  private users: User[] = [
    {
      id: 1,
      name: "John Doe",
      email: "johndoe@gmail.com",
      team: teams.get(1) as Team,
    },
    {
      id: 2,
      name: "Jane Doe",
      email: "janedoe@gmail.com",
      team: teams.get(2) as Team,
    },
    {
      id: 3,
      name: "Mike Doe",
      email: "mikedoe@gmail.com",
      team: teams.get(3) as Team,
    },
  ];
  @Query(() => [User])
  async getUsers(): Promise<User[]> {
    return this.users;
  }
  @Query(() => User)
  async getUser(@Arg("id") id: number): Promise<User | undefined> {
    const user = this.users.find((u) => u.id == id);
    return user;
  }
  @Mutation(() => User)
  async updateUser(
    @Arg("id") id: number,
    @Arg("input") input: UserInput
  ): Promise<User> {
    const user = this.users.find((u) => u.id == id);
    if (!user) {
      throw new Error("User not found");
    }
    const updatedUser = {
      ...user,
      ...input,
    };
    this.users = this.users.map((u) => (u.id === id ? updatedUser : u));
    return updatedUser;
  }
}
