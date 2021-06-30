result = ''
loop do
    puts result
    puts "Programa para aferir a idade de uma pessoa."
    puts "Digite 1 para continuar"
    puts "DIgite 0 para sair "
    op = gets.chomp.to_i
    if op==0
        break
    elsif op==1
        puts "Digite o ano que você nasceu:"
        ano_nas = gets.chomp.to_i
        puts "Digite o ano atual: "
        ano_atual = gets.chomp.to_i
        result = "Quem nasceu no ano #{ano_nas} tem hoje #{ano_atual-ano_nas} de idade"
    else
        puts "Opção inválida, tente novamente."
    end
    system "clear"
end

