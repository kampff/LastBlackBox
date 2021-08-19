// ALU Decoder
module alu_decoder(opcode_b5, funct3, funct7b5, ALU_op, ALU_control);

    // Declarations
    input opcode_b5;
    input [2:0] funct3;
    input funct7b5;
    input [1:0] ALU_op;
    output reg [2:0] ALU_control;

    // Intermediates
    wire R_type_subtract;
    assign R_type_subtract = funct7b5 & opcode_b5; // TRUE for R–type subtract   
    
    // Logic
    always @*
        case(ALU_op)
            2'b00: ALU_control = 3'b000; // addition   
            2'b01:
                case(funct3)
                    3'b000: ALU_control = 3'b001; // subtraction (beq)
                    3'b001: ALU_control = 3'b100; // xor (bne) - could use subtraction?
                    default: ALU_control = 3'bxxx; // ???
                endcase
            default:
                case(funct3) // R–type or I–type ALU
                    3'b000: 
                        begin
                            if (R_type_subtract)
                                ALU_control = 3'b001; // sub
                            else
                                ALU_control = 3'b000; // add, addi
                        end
                    3'b010: ALU_control = 3'b101; // slt, slti
                    3'b100: ALU_control = 3'b100; // xor, xori
                    3'b110: ALU_control = 3'b011; // or, ori
                    3'b111: ALU_control = 3'b010; // and, andi
                    default: ALU_control = 3'bxxx; // ???
                endcase
        endcase

endmodule

// Add XOR for beq