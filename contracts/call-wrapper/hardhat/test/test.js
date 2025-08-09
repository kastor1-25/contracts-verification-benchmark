const {
    loadFixture
} = require("@nomicfoundation/hardhat-toolbox/network-helpers");

const { expect } = require("chai");

/*
        CallWrapper1
*/

describe("CallWrapper1", function () {

    async function deployContract() {

        const SelfDestructOnCall = await ethers.deployContract("SelfDestructOnCall", {
            value: ethers.parseUnits("100", "wei")
        });

        const CallWrapper = await ethers.deployContract("CallWrapper1");

        return { SelfDestructOnCall, CallWrapper };
    };

    it("Balance changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, CallWrapper } = await loadFixture(deployContract);

        const balanceBefore = await ethers.provider.getBalance(CallWrapper);

        await CallWrapper.callwrap(SelfDestructOnCall);

        const balanceAfter = await ethers.provider.getBalance(CallWrapper);

        expect(balanceAfter).not.to.equal(balanceBefore);
    });
});

/*
        CallWrapper2
*/

describe("CallWrapper2", function () {

    async function deployContract() {

        const SelfDestructOnCall = await ethers.deployContract("SelfDestructOnCall", {
            value: ethers.parseUnits("100", "wei")
        });

        const CallWrapper = await ethers.deployContract("CallWrapper2");

        return { SelfDestructOnCall, CallWrapper };
    };

    it("Balance changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, CallWrapper } = await loadFixture(deployContract);

        const balanceBefore = await ethers.provider.getBalance(CallWrapper);

        await CallWrapper.callwrap(SelfDestructOnCall);

        const balanceAfter = await ethers.provider.getBalance(CallWrapper);

        expect(balanceAfter).not.to.equal(balanceBefore);
    });
});

/*
        CallWrapper3
*/

describe("CallWrapper3", function () {

    async function deployContract() {
        const ChangeDataOnCall = await ethers.deployContract("ChangeDataOnCall");

        const SelfDestructOnCall = await ethers.deployContract("SelfDestructOnCall", {
            value: ethers.parseUnits("100", "wei")
        });

        const CallWrapper = await ethers.deployContract("CallWrapper3");

        return { SelfDestructOnCall, ChangeDataOnCall, CallWrapper };
    };
    
    it("Balance changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, ChangeDataOnCall, CallWrapper } = await loadFixture(deployContract);
        
        const balanceBefore = await ethers.provider.getBalance(CallWrapper);

        await CallWrapper.callwrap(SelfDestructOnCall);

        const balanceAfter = await ethers.provider.getBalance(CallWrapper);

        expect(balanceAfter).not.to.equal(balanceBefore);
    });

    it("Storage changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, ChangeDataOnCall, CallWrapper } = await loadFixture(deployContract);

        const storageBefore = await ethers.provider.getStorage(CallWrapper, 0);
        await CallWrapper.callwrap(ChangeDataOnCall);

        const storageAfter = await ethers.provider.getStorage(CallWrapper, 0);

        expect(storageAfter).not.to.equal(storageBefore);
    });

});

/*
        CallWrapper4
*/

describe("CallWrapper4", function () {

    async function deployContract() {
        const ChangeDataOnCall = await ethers.deployContract("ChangeDataOnCall");

        const SelfDestructOnCall = await ethers.deployContract("SelfDestructOnCall", {
            value: ethers.parseUnits("100", "wei")
        });

        const CallWrapper = await ethers.deployContract("CallWrapper3");

        return { SelfDestructOnCall, ChangeDataOnCall, CallWrapper };
    };
    
    it("Balance changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, ChangeDataOnCall, CallWrapper } = await loadFixture(deployContract);

        const balanceBefore = await ethers.provider.getBalance(CallWrapper);

        await CallWrapper.callwrap(SelfDestructOnCall);

        const balanceAfter = await ethers.provider.getBalance(CallWrapper);

        expect(balanceAfter).not.to.equal(balanceBefore);
    });

    it("Storage changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, ChangeDataOnCall, CallWrapper } = await loadFixture(deployContract);

        const storageBefore = await ethers.provider.getStorage(CallWrapper, 0);
        await CallWrapper.callwrap(ChangeDataOnCall);

        const storageAfter = await ethers.provider.getStorage(CallWrapper, 0);

        expect(storageAfter).not.to.equal(storageBefore);
    });

});

/*
        CallWrapper5
*/

describe("CallWrapper5", function () {

    async function deployContract() {

        const SelfDestructOnCall = await ethers.deployContract("SelfDestructOnCall", {
            value: ethers.parseUnits("100", "wei")
        });

        const CallWrapper = await ethers.deployContract("CallWrapper5");

        return { SelfDestructOnCall, CallWrapper };
    };

    it("Balance changes after a call to `callwrap()`", async function () {

        const { SelfDestructOnCall, CallWrapper } = await loadFixture(deployContract);

        const balanceBefore = await ethers.provider.getBalance(CallWrapper);

        await CallWrapper.callwrap(SelfDestructOnCall);

        const balanceAfter = await ethers.provider.getBalance(CallWrapper);

        expect(balanceAfter).not.to.equal(balanceBefore);
    });
});
