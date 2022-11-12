import "reflect-metadata";
import { Query, Resolver, Arg } from "type-graphql";
import { getInstance } from "../db";
import { Team } from "./teams.schema";

@Resolver(() => Team)
export class TeamsResolver {
  @Query(() => Team)
  async getTeam(@Arg("id") id: number): Promise<Team | undefined> {
    const db = await getInstance();
    const ret = await db.all(`select id, name from teams where id=?`, id);
    if (ret.length === 0) {
      return undefined;
    }
    if (ret.length > 1) {
      throw new Error(`multiple record with id =${id}`);
    }
    const obj = ret[0];
    return {
      id: obj.id,
      name: obj.name,
    };
  }
}
