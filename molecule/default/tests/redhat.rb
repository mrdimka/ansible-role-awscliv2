# frozen_string_literal: true

# Molecule managed

describe command('aws') do
  it { should exist }
end

describe command('aws_completer') do
  it { should exist }
end
