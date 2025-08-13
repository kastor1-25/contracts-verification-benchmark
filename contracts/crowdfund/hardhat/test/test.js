const { loadFixture, mine } =
    require("@nomicfoundation/hardhat-toolbox/network-helpers");
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("Crowdfund - reclaim reverts", function () {
    async function deployContract() {
        const [owner] = await ethers.getSigners();

        const nowBlock = await ethers.provider.getBlockNumber();
        const endDonate = nowBlock + 5;

        const goal = ethers.parseEther("1000");

        const crowdfund = await ethers.deployContract("Crowdfund", [
            await owner.getAddress(),
            endDonate,
            goal,
        ]);

        const donor = await ethers.deployContract("RevertOnReceive");

        await donor.setCrowdfund(await crowdfund.getAddress());

        await donor.donate({ value: ethers.parseEther("1") });

        const current = await ethers.provider.getBlockNumber();
        const toMine = Math.max(1, endDonate - current + 1);
        await mine(toMine);

        return { crowdfund, donor, owner};
    }

    it("reclaim() reverts if the donor's receive() reverts", async function () {
        const { donor } = await loadFixture(deployContract);

        await expect(donor.reclaim()).to.be.reverted;
    });
});

describe("Crowdfund - withdraw reverts", function () {
    async function deployContract() {
        const [donor] = await ethers.getSigners();

        const nowBlock = await ethers.provider.getBlockNumber();
        const endDonate = nowBlock + 5;

        const goal = ethers.parseEther("1");

        const owner = await ethers.deployContract("RevertOnReceive");

        const crowdfund = await ethers.deployContract("Crowdfund", [
            await owner.getAddress(),
            endDonate,
            goal,
        ]);

        await owner.setCrowdfund(await crowdfund.getAddress());

        await crowdfund.connect(donor).donate({ value: ethers.parseEther("1.1") });

        const current = await ethers.provider.getBlockNumber();
        const toMine = Math.max(1, endDonate - current + 1);
        await mine(toMine);

        return { crowdfund, owner, donor };
    }

    it("withdraw() reverts if the owner's receive() reverts", async function () {
        const { owner } = await loadFixture(deployContract);
        await expect(owner.withdraw()).to.be.reverted;
    });
});

describe("Crowdfund - forced ETH via selfdestruct after donation phase", function () {
  async function deployFixture() {
    const [owner] = await ethers.getSigners();

    const nowBlock = await ethers.provider.getBlockNumber();
    const endDonate = nowBlock  - 1; 
    const goal = ethers.parseEther("1000"); 

    const crowdfund = await ethers.deployContract("Crowdfund", [
      await owner.getAddress(),
      endDonate,
      goal,
    ]);

    const selfDestruct = await ethers.deployContract("SelfDestruct", [], {
      value: ethers.parseEther("1"),
    });
    await selfDestruct.setCrowdfund(crowdfund.target);

    return { crowdfund, selfDestruct };
}

  it("after the end_donate, the crowdfund contract can still receive ETH via selfdestruct", async function () {
    const { crowdfund, selfDestruct } = await loadFixture(deployFixture);

    const before = await ethers.provider.getBalance(crowdfund.target);

    const tx = await selfDestruct.selfDestruct();
    await tx.wait();

    const after = await ethers.provider.getBalance(crowdfund.target);

    expect(before).to.be.lessThan(after);
  });
});